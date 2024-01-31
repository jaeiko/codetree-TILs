'''
dx, dy 테크닉을 활용한 문제 7

1초에 한 칸씩 움직이며, 회전에도 1초의 시간이 걸린다 했을 때, 
몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단하는 프로그램

N개의 명령에 따라 총 N번 움직이며, 명령 L이 주어지면 왼쪽으로 90도 방향 전환을, 
명령 R이 주어지면 오른쪽으로 90도 방향전환을 하고, 
명령 F가 주어지면 바라보고 있는 방향으로 한칸 이동
'''

import sys

# 명령 입력
commands = input()

    # N  E  S  W
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# time, (x, y), dir_num값 초기화
time = 0    # 총 소요시간
x, y = 0, 0 # 좌표
dir_num = 0 # 방향 설정용

for elem in commands:
    if elem == 'F': # 명령 F이면 이동
        x, y = x + dx[dir_num], y + dy[dir_num]
    elif elem == 'L':   # 명령 L이면 왼쪽으로 90도 회전 전환
        dir_num = (dir_num + 1) % 4
    elif elem == 'R':   # 명령 R이면 오른쪽으 90도 회전 전환
        dir_num = (dir_num + 3) % 4

    time += 1   # 1초 증가

    if x == 0 and y == 0:   # 원점으로 다시 되돌아왔다면 시간 출력 후 프로그램 종료
        print(time)
        sys.exit(0)

# N번 이동을 진행했는데도 시작점으로 돌아오지 못했다면 -1을 출력
print(-1)