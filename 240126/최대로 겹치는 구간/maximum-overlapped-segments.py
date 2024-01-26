# 입력 횟수 n
n = int(input())

OFFSET = 100    # OFFSET 100으로 설정(음수가 아닌 0 이상의 범위로 정하기 위해)

line = [0] * 200  # x1:0 ~ x2:200 의 선분

for i in range(n):
    x1, x2 = tuple(map(int, input().split()))   # 겹칠 구간 x1~x2 입력
    x1 += OFFSET
    x2 += OFFSET
    for j in range(x1, x2): # 겹치는 구간에 1증가
        line[j] += 1

print(max(line))