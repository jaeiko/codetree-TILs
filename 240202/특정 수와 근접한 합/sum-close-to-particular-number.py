'''
완전탐색 문제

정수 S와 N개의 수가 주어지면, N개의 수들 중 정확히 2개를 제외하여 남은 N-2개의 숫자들의 합이 S와 최대한 가까워지도록 하는 프로그램
'''
# 정수 개수 n과 비교 대상 정수 s 입력
n, s = tuple(map(int, input().split()))

# 입력받은 정수 저장하는 리스트
num_arr = list(map(int, input().split()))
# 차이값 저장하는 리스트
dif_arr = []

# 완전탐색 기법
for i in range(n):
    sum_val = 0
    for j in num_arr[i+1::]:
        sum_val += j
    dif_arr.append(abs(sum_val - s))

# 정수 s와의 차이값 중 최소값 출력
print(min(dif_arr))