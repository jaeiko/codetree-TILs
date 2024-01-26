n = int(input())

# - 100 ~ 100 => 0 ~ 200
OFFSET = 100

# 200 * 200 보드판 생성
board = [
    [0] * 201
    for _ in range(201)
]

for i in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))   # x1, y1, x2, y2 입력

    # 음수 범위 => 0 이상의 범위로 바꿔야하므로 OFFSET 설정
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    # 해당 범위만큼 1로 변경
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

# 넓이
area = 0
for i in range(201):
    for j in range(201):
        if board[i][j] == 1:
            area += 1

# 출력
print(area)