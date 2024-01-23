arr = [ # 4*4 배열 입력
    list(map(int, input().split()))
    for _ in range(4)
]

sum = 0
for i in range(4):
    for j in range(i + 1):
        if j == 4:
            break
        sum += arr[i][j]

print(sum)