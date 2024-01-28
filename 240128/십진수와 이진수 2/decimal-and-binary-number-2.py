'''
이진수로 표현되는 N이 주어지면 십진수로 바꿔 17배를 하고 다시 이진수로 나타내어 출력하는 프로그램
'''

# 2진수 입력
binary = list(map(int, input()))

# 10진수 변수
decimal = 0

# 2진수 -> 10진수 변환
for elem in binary:
    decimal = decimal * 2 + elem    # 2진수 -> 10진수 변환

# 10진수값을 17배하여 다시 decimal에 저장
decimal = decimal * 17

# 변환한 2진수 값을 담기 위해 binary를 리스트로 초기화
binary = []

# 10진수 -> 2진수 변환
while True:
    if decimal == 0:   # 더 이상 나눌게 없으면 break
        break
    binary.append(decimal % 2)
    decimal //= 2

# 2진수 결과 출력
for elem in binary[::-1]:
    print(elem, end='')