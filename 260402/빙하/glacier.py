from collections import deque

n, m = map(int, input().split())    # n * m
grid = [list(map(int, input().split())) for _ in range(n)]  # grid
visited = [[0] * m for _ in range(n)]   # 기존에 방문했는지 체크하는 함수
outside_ice_coor = []   # 바깥 빙하 좌표 저장하는 리스트

q = deque()

time = 0    # 시간
ice_count = sum(row.count(1) for row in grid)   # 남아있는 ice 개수(우선 처음에도 남아있는 빙하개수 저장)


# Please write your code here.
# 1. 가장 바깥 부분은 항상 빙하가 아님. 그래서 가장 바깥 부분 중 하나를 시작 좌표로 잡고 시작해도 될 듯.
# 2. bfs로 탐색하면서 빙하 맞닿아 있으면 해당 칸 -= 1
# 3. 빙하로 둘러싸여있는 물의 경우 붙어있는 빙하를 녹이지 못함. 근데 어차피 둘러쌓여 있으면 bfs 탐색상 들어가지 못하니 평소대로 bfs 코딩하면 됨.
# 4. 바깥부분 -= 1을 다 한 후, 남아있는 빙하 수 카운트와 동시에 시간도 카운트
# 5. 결과 출력

# dxs, dys 테크닉
dxs = [1, 0, 0, -1]
dys = [0, -1, 1, 0]

# 배열 범위 체크 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 갈 수 있는지 체크하는 함수
def can_go(x, y):
    # 범위 밖이면 갈 수 없으니 False
    if not in_range(x, y):
        return False
    
    # 이미 방문한 적 있으면 해당 좌표의 visited를 1로 체크
    if visited[x][y] == 1:
        return False

    # 해당 좌표가 빙하인 경우 해당 빙하 좌표 추가 한 뒤 False
    if grid[x][y] == 1:
        outside_ice_coor.append((x, y))
        return False

    return True

# push 함수
def push(x, y):
    visited[x][y] = 1
    q.append((x, y))

# bfs 함수
def bfs():
    while q:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy
            if can_go(nx, ny):
                push(nx, ny)

while True: 
    push(0, 0)
    bfs()   # bfs 실행

    # 바깥쪽 빙하들은 0으로 바꾸기
    for x, y in outside_ice_coor:
        grid[x][y] = 0
    
    can_coor = []   # 다음 bfs 탐색을 위해 초기화
    time += 1   # bfs 한번 다 돌면 사실상 시간 1초 증가이니 time += 1
    
    # 남아있는 빙하 개수 카운트한 후, 0개가 아닌 이상 저장하기
    check_ice = sum(row.count(1) for row in grid)
    if (check_ice != 0):
        ice_count = check_ice
    else:   # 남아있는 빙하 개수가 0개되면 반복문 탈출하고 정답 출력하기
        break

    # 다음 bfs 탐색을 위해 visited 초기화
    visited = [[0] * m for _ in range(n)]

# 시간, 남아있는 빙하 개수 출력
print(time, ice_count)