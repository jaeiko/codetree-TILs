'''
dx, dy 테크닉을 활용한 문제 8

시작 위치를 포함하여 위치를 이동하게 될 때마다 해당 칸에 적혀있는 수를 계속 더한다고 헀을 때, 
이들의 총합을 구하는 프로그램을 구하는 프로그램

명령 L은 왼쪽으로 90도 방향 전환을, 
명령 R은 오른쪽으로 90도 방향 전환을, 
명령 F가 주어지면 바라보고 있는 방향으로 한칸 이동하게 된다. 
'''

# x, y가 배열 범위 내에 있는지 체크하는 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# n, t 입력 (n : n * n 크기의 정사각형, t : 명령 횟수)
n, t = tuple(map(int, input().split()))

# 명령 입력
commands = input()

# n * n 행렬의 요소 입력
arr = [
    input().split()
    for _ in range(n)
]

    # R  D  L   U
dx = [-1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 가운데 위치에서 북쪽을 향한 상태로 움직이는 것을 시작
x, y = n//2 , n//2
dir_num = 0 # 방향 전환용 변수

# sum_val 값에 arr[n//2][n//2] 저장
sum_val = arr[x][y]

for elem in commands:
    if elem == 'R':     # 명령 R은 오른쪽으로 90도 방향 전환
        dir_num = (dir_num + 1) % 4
    elif elem == 'L':   # 명령 L은 왼쪽으로 90도 방향 전환
        dir_num = (dir_num + 3) % 4
    elif elem == 'F':   # 명령 F가 주어지면 바라보고 있는 방향으로 한칸 이동
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        print(nx, ny)
        if not in_range(nx, ny):  # 격자의 범위를 벗어나게 하는 명령어는 무시해야함
            continue
        x, y = nx, ny
        sum_val += int(arr[x][y])

# 출력
print(sum_val)