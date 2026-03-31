from collections import deque
from itertools import combinations
import sys

# n: 격자의 크기 / k: 시작점의 수 / m: 치워야 할 돌의 개수
n, k, m = map(int, input().split())
# grid: 맵 정보
grid = [list(map(int, input().split())) for _ in range(n)]
# stone: 돌의 좌표 저장
# key point: 이렇게 2차원 배열에서 조건에 맞는 값의 좌표를 찾는 방법 알아두기!!
stone = [(r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 1]
# stone_combi: 돌의 좌표들에서 가능한 m개를 선택하는 조합들로 이루어진 리스트(나중에 지우기 위해)
# key point: 꼭 combinations 쓰는 법 알아두기!!(매우 편함)
stone_combi = list(combinations(stone, m))
# start_info: 시작점 정보 추가(e.g. [(1,2), (3,4)]...)
start_info = list(tuple(map(int, input().split())) for _ in range(k))

# max_num: 돌을 제거했을 때 가능한 최댓값 저장하는 변수
max_num = -sys.maxsize

# 방문 여부 리스트
visited = [[0] * n for _ in range(n)]

#bfs_count: start_x, start_y에서 시작할 때 방문 가능한 횟수
bfs_count = 0

# tot_count: 모든 start_x, start_y에서 시작을 포함해서 총 방문 가능한 횟수
tot_count = 0

q = deque()

# Please write your code here.
# dxs, dys 테크닉
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

# 배열 범위 밖인지 체크하는 함수
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 해당 위치에서 갈수 있는지 체크하는 함수
def can_go(x, y):
    if not in_range(x, y):  # 범위 밖이면 False
        return False
    
    if visited[x][y] or grid[x][y] == 1:   # 이미 방문한 적이 있다면 False
        return False
    
    return True

def push(x, y):
    global bfs_count
    # 이전에 방문한 적 없던 곳이면 bfs_count += 1
    if visited[x][y] == False:
        bfs_count += 1
    visited[x][y] = True
    q.append((x, y))


def bfs():
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):  # 옆 동네 갈 수 있으면 큐에 추가
                push(nx, ny)
    
    return bfs_count



if len(stone) == 0: # 돌의 개수가 하나도 없다면 그냥 bfs 수행
    for start_x, start_y in start_info:
        push(start_x-1, start_y-1)   # 인덱스 0을 기준으로 하니 - 1
        tot_count += bfs()

    # 정답 출력
    print(tot_count)
else:   # 돌의 개수가 있으면 m개만큼 지우고 bfs 수행해서 도달 가능한 칸의 최댓값을 저장하기
    for i in range(len(stone_combi)):
        # 1. stone_combi[i] 일 때의 돌들을 일단 제거
        for stone_x, stone_y in stone_combi[i]:
            grid[stone_x][stone_y] = 0
            
        # 2. bfs 수행해서 방문 가능한 수 체크
        for start_x, start_y in start_info:
            push(start_x-1, start_y-1)
            tot_count += bfs()
            bfs_count = 0
            
        # 3. 최댓값을 정답 변수인 max_num에 저장
        max_num = max(max_num, tot_count)
        
        # 다음 경우의 수를 위해 tot_count를 0으로 초기화
        tot_count = 0

        # 3. 다음 경우의 수를 위해 돌 원상복귀
        for stone_x, stone_y in stone_combi[i]:
            grid[stone_x][stone_y] = 1

        # 4. 다음 경우의 수를 위해 다시 visited 0으로 초기화
        visited = [[0] * n for _ in range(n)]
    
    # 정답 출력: 다 제거 조합을 고려해봤을 때 방문 가능한 최댓값 출력
    print(max_num)