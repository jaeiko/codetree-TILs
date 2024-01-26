# 2000 * 2000 크기의 보드판
board = [
    [0] * 2001
    for _ in range(2001)
]

# OFFSET 1000 설정 : -1000~1000 -> 0~2000
OFFSET = 1000

# 넓이 색칠하기
for i in range(3):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    # 해당 범위만큼 1로 변경
    for j in range(x1, x2):
        for k in range(y1, y2):
            if i == 2:
                board[j][k] = 0
            else:
                board[j][k] = 1

# 넓이
area = 0
for i in range(2001):
    for j in range(2001):
        if board[i][j] == 1:
            area += 1

# 출력
print(area)