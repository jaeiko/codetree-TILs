# 입력 횟수 n
n = int(input())

line = [0] * 200  # x1:0 ~ x2:200 의 선분

for i in range(n):
    x1, x2 = tuple(map(int, input().split()))   # 겹칠 구간 x1~x2 입력
    if x1 < 0 : # 만약 x1이 음수이면 그 x1만큼 절댓값을 더해서 양수로 설정
        x1 += abs(x1)
        x2 += abs(x1)
    for j in range(x1, x2): # 겹치는 구간에 1증가
        line[j] += 1

print(max(line))