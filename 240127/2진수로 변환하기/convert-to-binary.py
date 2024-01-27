'''
십진수 n이 주어지면 0과 1로만 이루어진 2진수로 그 수를 변환하여 출력하는 프로그램
'''

# 정수 n 입력
n = int(input())
digits = [] # 2진수 리스트

while True:
    if n < 2:       # 만약 n이 2 미만이면 n을 digits에 추가 후 break
        digits.append(n)
        break

    # n을 2로 나눈 나머지를 digits에 추가
    digits.append(n % 2)
    n //= 2 # n을 2로 나눈 몫을 n에 저장

# break 후 2진수 출력
for digit in digits[::-1]:
    print(digit, end='')