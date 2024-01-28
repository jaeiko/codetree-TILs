'''
빨간색, 파란색 순으로 번갈아 가며 주어지고, 겹치는 위치가 있다면 가장 마지막에 덮힌 색으로 취급한다고 했을 때,
 n개의 직사각형이 주어지고 난 뒤의 파란색 영역의 총 넓이를 구하는 프로그램
'''

# 입력할 직사각형의 개수 n 입력
n = int(input())

# 200 * 200 크기의 보드판
board = [
    [0] * 201
    for _ in range(201)
]

# OFFSET 설정 : -100 ~ 100 -> 0 ~ 200
OFFSET = 100

# 초기 색깔 : 빨강
color = 'R'

for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))   # 한 직사각형의 x1, y1, x2, y2 입력

    # 좌표의 OFFSET 설정(음수 범위를 없애고 양수범위에서 좌표를 놓기 위해)
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = color # 해당 넓이만큼 색깔 칠하기

    if color == 'R':    # 이번이 빨강색 사각형이였다면 파란색 사각형으로 변경
        color = 'B'
    else:               # 이번이 파란색 사각형이였다면 빨간 사각형으로 변경
        color = 'R'

# 파란색 영역 넓이 구하기
blue_area = 0
for row in board:
    for elem in row:
        if elem == 'B':
            blue_area += 1

# 출력
print(blue_area)