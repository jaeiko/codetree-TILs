'''
완전탐색 문제

n개의 숫자가 주어지고, 특정 구간을 잡았을 때 그 구간 안에 있는 원소들의 평균값이 그 구간의 원소 중 하나가 되는 서로 다른 가짓수를 구하는 프로그램
'''

# n 입력
n = int(input())

# n개의 숫자 입력
arr = list(map(int, input().split()))

# 먼저 구간이 [k, k] 인 경우는 구간 안에 원소가 하나밖에 으므로 평균이 곧 그 원소가 됨! => cnt에 n 증가시키고 시작
cnt = n

# 완전탐색
for i in range(n-1):
    for j in range(i+1, n):
        if sum(arr[i:j+1]) / len(arr[i:j+1]) in arr[i:j+1]:
            cnt += 1

print(cnt)