'''
완전탐색 문제

문자열이 주어지면 총 'COW’가 순서대로 가능한 가짓수를 출력하는 프로그램
'''

# 문자열의 길이 n 입력
n = int(input())

# 문자열 입력
string = input()

# 완전탐색
cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if string[i] == 'C' and string[j] == 'O' and string[k] == 'W':
                cnt += 1

# 출력
print(cnt)