'''
완전탐색 문제

3마리의 서로 다른 소의 위치를 (i, j, k)라고 했을 때, i < j < k를 만족하며 
동시에 Ai <= Aj <= Ak를 만족하는 서로 다른 쌍의 수를 구하는 프로그램
'''

# 소 마릿수 n
n = int(input())

arr = list(map(int, input().split()))

cnt = 0 # 위의 조건을 만족하는 서로 다른 쌍의 수를 저장하는 변수

# 완전 탐색
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] <= arr[j] <= arr[k]:
                cnt += 1

# 출력
print(cnt)