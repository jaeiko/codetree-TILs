import sys
from collections import deque
from itertools import combinations

# 입력 처리
# input() 대신 sys.stdin.readline()을 사용하여 입력 속도를 최적화
n, k, u, d = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 1. 맵에 존재하는 모든 격자의 좌표 리스트 생성
coor_info = [(r, c) for r in range(n) for c in range(n)]

# 2. 가능한 모든 시작 도시(k개)의 조합 생성
start_city_combinations = list(combinations(coor_info, k))

# 상하좌우 방향 배열
dxs = [-1, 0, 0, 1]
dys = [0, 1, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

max_ans = 0

# 3. 각 조합에 대해 BFS 탐색 진행
for start_cities in start_city_combinations:
    # 매 조합마다 방문 배열을 새롭게 초기화
    visited = [[False] * n for _ in range(n)]
    q = deque()

    # 선택된 k개의 시작 도시를 큐에 넣고 미리 방문 처리
    for x, y in start_cities:
        q.append((x, y))
        visited[x][y] = True

    # BFS 실행
    while q:
        curr_x, curr_y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            # 격자 범위 내에 있고 아직 방문하지 않은 도시라면
            if in_range(new_x, new_y) and not visited[new_x][new_y]:
                # 현재 도시와 이동할 도시 간의 높이 차이 계산
                diff = abs(grid[curr_x][curr_y] - grid[new_x][new_y])
                
                # 높이 차이가 조건(u 이상 d 이하)을 만족하는지 확인
                if u <= diff <= d:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))

    # 탐색 종료 후, 현재 조합에서 방문 가능한 총 도시 수 계산
    # 리스트 컴프리헨션을 활용하여 2차원 배열 내의 True 개수를 합산
    current_count = sum(row.count(True) for row in visited)
    
    # 최댓값 갱신
    max_ans = max(max_ans, current_count)

print(max_ans)