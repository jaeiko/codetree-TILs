'''
완전탐색 문제

n개의 숫자가 주어졌을 때, 인접하지 않은 2개의 숫자를 적절하게 골라 합이 최대가 되도록 하는 프로그램
'''
import sys

n = int(input())

arr = list(map(int, input().split()))

max_val = -sys.maxsize

# 완전탐색
for i in range(n-1):
    for j in range(i+2, n):
        if arr[i] + arr[j] > max_val:
            max_val = arr[i] + arr[j]

# 출력
print(max_val)