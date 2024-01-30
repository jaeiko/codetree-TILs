# 좌표평면 위 (0, 0)에서 북쪽을 향한 상태
dir_num = 3 
x, y = 0, 0

# dx, dy 테크닉(동, 남, 서, 북)
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# 입력받은 명령을 하나씩 분리하여 command_list에 저장
command_list = list(input())

for elem in command_list:
# 회전 방향 : 원래 방향의 90도로 변경
    if elem == 'L':  # L이면 반시계 방향으로 90도 회전
        dir_num = (dir_num - 1 + 4) % 4
    elif elem == 'F': # F이면 move
        x += dx[dir_num]
        y += dy[dir_num]

# 결과값 출력
print(x, y)