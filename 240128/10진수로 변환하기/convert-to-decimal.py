'''
0과 1로 이루어진 2진수로 어떤 수가 주어지면 그 수를 십진수로 변환하여 출력하는 프로그램
'''

# 2진수 입력 (ex. 11101 -> [1, 1, 1, 0, 1]) => 이 때 input() 대신 input().split() 사용하면 띄어쓰기 중심으로 판별하니 11101 자체를 하나의 묶음으로 인식되므로 주의
binary = list(map(int, input()))

# 10진수값 저장할 num 변수
num = 0

# 2진수 -> 10진수 변환
for elem in binary:
    num = num * 2 + int(elem)

# 10진수 출력
print(num)