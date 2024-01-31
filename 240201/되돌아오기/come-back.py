'''
dx, dy 테크닉을 활용한 문제 6

N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어지고, 1초에 한 칸씩 움직인다고 했을 때, 
몇 초 뒤에 처음으로 다시 (0, 0)에 돌아오게 되는지를 판단하는 프로그램
'''
import sys

# 움직일 총 횟수 n
n = int(input())

    # N  E  S  W
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# mapper dict
mapper = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3
}

# x, y, nx, ny, time 0으로 초기화
x, y = 0, 0
time = 0

for i in range(n):
    direction, distance = tuple(map(str, input().split()))   # 방향, 이동거리 입력
    distance = int(distance)

    dir_num = mapper[direction]

    for _ in range(distance):   
        x, y = x + dx[dir_num], y + dy[dir_num] # move
        time += 1   # 움직인 거리 한 칸은 1초와 같음

        # 움직이고 난 뒤의 좌표가 원점이 되었다면 time 출력 후 프로그램 종료
        if x == 0 and y == 0:
            print(time)
            sys.exit(0)

# 최종 반복문 돌고 나서도 원점으로 못 갔으면 -1 출력 후 종료
print(-1)