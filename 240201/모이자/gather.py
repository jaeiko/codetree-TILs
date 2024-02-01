'''
완전탐색 문제

적절한 집을 선택하여 모든 사람들의 이동 거리의 합이 최소가 되도록 하는 프로그램
'''

import sys

# 최솟값
min_val = sys.maxsize

# 집의 갯수 n 입력
n = int(input())

# n개의 집에서 각각 살고 있는 사람의 수 입력해서 arr에 저장
arr = list(map(int, input().split()))

for i in range(n):
    sum_val = 0
    for j in range(n):
        sum_val += arr[j] * abs(i - j)  # i번째 집으로 모일 때, 모든 사람들의 이동 거리의 합을 구하고, 최솟값을 구함.
    min_val = min(sum_val, min_val)

# 출력
print(min_val)