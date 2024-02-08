'''
완전탐색 문제

n개의 숫자들이 주어졌을 때, 연속하여 k개의 숫자를 골랐을 때의 합이 최대가 되도록 하는 프로그램
'''

# n, k 입력
n, k = tuple(map(int, input().split()))

# n개의 숫자 입력
arr = list(map(int, input().split()))

# 완전탐색 (ex. n=6, k=3, 9 1 2 4 7 1 로 입력받았을 때 인덱스 0부터 3까지 돌려서 3개씩 완전탐색 : [9, 1, 2], [1, 2, 4], [2, 4, 7], [4, 7, 1])
sum_val = 0
for i in range(n-k+1):
    if sum_val < sum(arr[i:k+i]):
        sum_val = sum(arr[i:k+i])

# 출력
print(sum_val)