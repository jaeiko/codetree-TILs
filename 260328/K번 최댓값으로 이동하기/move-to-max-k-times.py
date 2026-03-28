from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c= map(int, input().split()) # 초기 시작위치 - r: 행, c: 열

x, y = r - 1, c - 1 # 배열 인덱스 특성상 -1

q = deque()

coor_info = list()

# Please write your code here.
#1. 시작 위치에서 갈 수 있는 지점들 중 시작 값보다 작으면서도 최댓값인 곳을 찾아야 함.
#1-1. 이떄 만족하는 숫자가 여러개일 경우, 행 번호가 가장 작은 곳, 열 번호가 가장 작은 곳 순으로 찾는다.
#2. 그 전에 시작 위치 주변이 시작값보다 둘러싸여 있으면 못가므로 종료해야 함.
#3. k번 반복문 돌았으면 그 뒤로 나오는 최종 값을 출력해야 함.

# dxs, dys
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

# 배열 범위 밖 벗어났는지 체크 여부
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(next_x, next_y, start_val):
    if not in_range(next_x, next_y):  # 범위 밖이면 False
        return False
    if visited[next_x][next_y] or grid[next_x][next_y] >= start_val:  # 이미 방문했거나 다음 방문 정보가 시작점 정보보다 값이 크다면 False
        return False
    
    return True

def push(x, y):
    visited[x][y] = True
    q.append((x, y))
    
def bfs(start_val):
    while q:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            next_x, next_y = curr_x + dx, curr_y + dy
            if can_go(next_x, next_y, start_val):
                push(next_x, next_y)
                coor_info.append((grid[next_x][next_y], (next_x, next_y)))    # 방문한 grid의 정보와 좌표도 따로 저장

for i in range(k):
    visited = [[0] * n for _ in range(n)]   # 방문했는지 체크하는 함수(매번 새 기준점 들어올때마다 초기화해야 한다.)
    current_start_val = grid[x][y]
    push(x, y)
    bfs(current_start_val)

    # coor_info는 이동가능한 좌표들의 모임. 즉, coor_info가 empty라면 이동할 수 있는 곳이 없기 떄문에 탐색을 종료.
    if not coor_info:
        break

    # 주의: count() 함수가 튜플 전체 구성 요소가 완전히 일치할 때만 개수를 센다!
    # 그러므로 특정 인덱스의 큰 값을 찾기 위해서는 아래처럼 써야 한다.
    # 값은 최대, 행은 최소, 열은 최소인 것을 한 번에 찾음
    # 참고로 파이썬의 max() 함수는 default 매개변수를 지원한다. max(coor_info, default=None, ...) 형태로 작성하면 리스트가 비어있을 때 에러를 뱉는 대신 None을 반환한다.
    # 근데 우리는 위에 if not coor_info를 했으니 굳이 쓸 필요는 없다.
    select_tuple = max(coor_info, key=lambda x: (x[0], -x[1][0], -x[1][1]))
    _, (x, y) = select_tuple
    coor_info = list()

# print answer
print(x+1, y+1)

# 이문제에서 알고 가야 할 포인트
# 1. 람다 사용법 숙지하기
# 2. 비교 기준은 계속 변동되는 curr_x, curr_y가 아닌 start_val인 점을 유의하자.