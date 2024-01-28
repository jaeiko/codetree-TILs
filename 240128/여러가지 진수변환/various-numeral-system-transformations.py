'''
정수 N이 주어지고, 바꿀 진수 B가 주어지면, 10진수인 정수 N을 B진수로 변경하여 출력하는 프로그램
'''

# 10진수 n, 바꿀 진수 b 입력(b로 주어지는 진수는 4, 8)
n, b = tuple(map(int, input().split()))

result = [] # 최종 변환 결과 변수

# 진수 변환
while True:
    if n == 0:  # 더 이상 나눌게 없으면 break
       break
    result.append(n % b)
    n //= b

# break 후 진수에 따른 결과 출력
for elem in result[::-1]:
    print(elem, end='')