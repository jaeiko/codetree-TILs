'''
반복 출력하기

정수 N이 주어지면, N개의 줄에 걸쳐 12345^&*()_를 출력하는 프로그램
'''

# n번 '12345^&*()_'를 출력하는 함수
def print_n_lines(n):
    for _ in range(n):
        print('12345^&*()_')

# 반복 횟수 n 입력
n = int(input())

# n을 print_n_lines 함수의 인자로 넘겨 실행
print_n_lines(n)