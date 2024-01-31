'''
dx, dy 테크닉을 활용한 문제 4

구슬의 처음 위치와 초기 방향이 주어졌을 때, t초가 지난 이후에 해당 구슬의 위치를 구하는 프로그램
이 때 범위는 1 ≤ r ≤ n, 1 ≤ c ≤ n | 2 ≤ n ≤ 50 | 1 ≤ t ≤ 100 임에 주의(인덱스가 1부터 시작)
'''

# x, y가 배열 안에 있는지 확인하는 함수
def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

    # 행렬에서의 L, D, R, U
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

# n : 격자의 크기
# t : 시간
n, t = tuple(map(int, input().split()))

# x, y : 현재 구슬의 위치
# d : 방향(R : right / D : down / U : up / L : left)
x, y, d = tuple(map(str, input().split()))
x = int(x)
y = int(y)
dir_num = mapper[d]

for i in range(t):
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    
    if in_range(nx, ny):    # check whether position is out of grid
        # 범위 내에 있으면 이동
        x, y = nx, ny
    else:
        # 범위 밖에 있으면 방향 전환
        dir_num = 3 - dir_num   # change direction

print(x, y)