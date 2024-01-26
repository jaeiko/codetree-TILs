# 반복 횟수 n
n = int(input())

line = [0] * 101    # 1~100

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))   # x1, x2 입력
    for i in range(x1, x2+1):   #x1~x2의 지점에 1증가
        line[i] += 1

가장 많이 겹치는 선분의 지점 출력
print(max(line))