'''
0과 1로 이루어진 2진수로 어떤 수가 주어지면 그 수를 십진수로 변환하여 출력하는 프로그램
'''

# 2진수 입력 (ex. 11101 -> [1, 1, 1, 0, 1])
binary = list(map(int, input()))

# 10진수값 저장할 num 변수
num = 0

# 2진수 -> 10진수 변환
for elem in binary:
    num = num * 2 + int(elem)

# 10진수 출력
print(num)