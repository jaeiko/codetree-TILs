'''
완전탐색 문제

N * N 격자를 벗어나지 않도록 1 * 3 크기의 격자를 적절하게 잘 잡아서 
해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램
'''
import sys

# 행렬의 크기 n과 n * n 격자 내의 배열 요소(동전 유 : 1 / 무 : 0) 입력
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

sum_val = 0 # 1 * 3 크기 격자 내에 들어올 수 있는 최대 동전의 수를 저장하는 변수
max_val = -sys.maxsize   # sum_val 중 최댓값 저장 변수

# 완전탐색
for i in range(n):
    for j in range(n-2):
        sum_val = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if max_val < sum_val:
            max_val = sum_val

# 출력
print(max_val)