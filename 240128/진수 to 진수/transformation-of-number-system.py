'''
정수 a와 b가 주어지고, a진수로 표현된 어떤 수 n이 주어지면, n을 b진수로 변환하여 출력하는 프로그램
'''
import sys

# n의 진수 a와 n을 변환할 진수 b 입력
a, b = tuple(map(int, input().split()))

# a진수로 표현된 n 입력
n = list(map(int, input()))

if a == b:  # a와 b가 같으면 진수가 같으니 그대로 n 출력하고 시스템 종료
    for elem in n:
        print(elem, end='')
    sys.exit(0)

# a진수로 표현된 n을 일단 10진수로 변환
decimal = 0
i = len(n)
for elem in n:
    decimal += elem * (a ** (i-1))
    i -= 1

# 다시 변환한 b진수로 저장하기 위해 n 을 빈 리스트로 초기화
n = []

# 10진수로 변환한 decimal을 b진수로 변환
while True:
    if decimal == 0:
        break
    
    n.append(decimal % b)
    decimal //= b

for elem in n[::-1]:
    print(elem, end='')