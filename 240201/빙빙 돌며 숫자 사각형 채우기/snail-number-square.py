'''
dx, dy 테크닉을 활용한 문제 5
n * m크기의 직사각형에 숫자 1부터 순서대로 증가시키며 달팽이 모양으로 채우는 코드

오른쪽(R) (direction = 0) : x는 그대로, y는 1 증가,
아래쪽(D) (direction = 1) : x는 1 증가, y는 그대로,
왼쪽(L) (direction = 2) : x는 그대로, y는 1 감소,
위쪽(U) (direction = 3) : x는 1 감소, y는 그대로

방향 전환 순서 : R -> D -> L -> U
'''
# x, y가 배열 범위 내에 있는지 체크하는 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# n, m 입력
n, m = tuple(map(int, input().split()))

# n * m 크기의 배열 생성(요소는 전부 0)
arr = [
    [0] * m
    for _ in range(n)
]

# x, y의 시작점과 시작점의 요소, 방향 초기화
x, y = 0, 0
dir_num = 0

# 방향(R | D | L | U)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1, n * m + 1):
    # 한칸 이동한 점인 nx, ny 설정
    arr[x][y] = i

    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if in_range(nx, ny) and arr[nx][ny] == 0: # nx, ny가 배열 범위 내에 있고 arr[nx][ny]가 아직 지나가지 않은 길인 경우 : keep going! 
        x, y = nx, ny
    else:   # 그 외의 경우 : 방향 전환
        dir_num = (dir_num + 1) % 4
        x, y = x + dx[dir_num], y + dy[dir_num]

# 출력
for col in arr:
    for elem in col:
        print(elem, end=' ')
    print()