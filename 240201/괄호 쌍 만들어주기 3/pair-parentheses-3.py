'''
완전탐색 문제

문자 '(', ')'로만 이루어진 문자열 A가 주어지면 그 문자열들 사이에서 여는 괄호와 닫는 괄호로 쌍을 이룰 수 있는 
서로 다른 가지수를 구하는 프로그램
'''


count = 0

# 문자 '(', ')'로만 이루어진 문자열 a
a = input()

# 완전 탐색
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] =='(' and a[j] == ')':
            count += 1

# 출력
print(count)