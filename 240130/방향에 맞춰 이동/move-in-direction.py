'''
(0, 0)에서 시작하여 총 N번 움직여보려고 한다. N번에 걸쳐 움직이려는 방향과 움직일 거리가 주어졌을 때, 최종 위치를 출력하는 프로그램
'''

n = int(input())

# 방향 리스트
direction_list = ['N', 'S', 'E', 'W']

x, y = 0, 0

for _ in range(n):
    direction, distance = tuple(map(str, input().split()))
    if direction == 'N':
        x, y = x, y + int(distance)
    elif direction == 'S':
        x, y = x, y - int(distance)
    elif direction == 'E':
        x, y = x + int(distance), y
    elif direction == 'W':
        x, y = x - int(distance), y

print(x, y)