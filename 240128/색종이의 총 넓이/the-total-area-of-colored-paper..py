'''
좌표평면위에 가로세로 길이가 8이고 넓이가 64인 색종이가 N장 주어졌다. 이 N장 색종이의 각 좌측하단의 꼭지점이 주어졌을 때 모든 색종이가 붙여진 이후의 총 넓이를 구하는 프로그램
'''

# 색종이 n장 입력
n = int(input())

# - 100 ~ 100 => 0 ~ 200
OFFSET = 100

# 200 * 200 보드판 생성
board = [
    [0] * 201
    for _ in range(201)
]

for i in range(n):
    x, y = tuple(map(int, input().split()))   # x, y 입력

    # 음수 범위 => 0 이상의 범위로 바꿔야하므로 OFFSET 설정
    x += OFFSET
    y += OFFSET

    # 해당 범위만큼 1로 변경
    for i in range(x, x+8):
        for j in range(y, y+8):
            board[i][j] = 1

# 넓이
area = 0
for i in range(201):
    for j in range(201):
        if board[i][j] == 1:
            area += 1

# 출력
print(area)