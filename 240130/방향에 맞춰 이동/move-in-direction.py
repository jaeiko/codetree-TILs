'''
(0, 0)에서 시작하여 총 N번 움직여보려고 한다. N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어졌을 때, 최종 위치를 출력하는 프로그램(dx, dy 테크닉 사용)
'''

# 움직일 횟수 n
n = int(input())

# 시작 위치
x, y = 0, 0

# dir_num : 방향 번호
dir_num = 0

# dx, dy 테크닉
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

for _ in range(n):
    direction, distance = tuple(map(str, input().split()))
    if direction == 'N':    # N이면 y축 방향으로 distance 증가
        dir_num = 0
    elif direction == 'S':  # S이면 y 축 방향으로 -distance 증가
        dir_num = 1
    elif direction == 'E':  # E이면 x 축 방향으로 distance 증가
        dir_num = 2
    elif direction == 'W':  # W이면 x 축 방향으로 -distance 증가
        dir_num = 3

    # 해당 방향으로 x와 y 증가
    x += int(distance) * dx[dir_num]
    y += int(distance) * dy[dir_num]

# 출력
print(x, y)