'''
1. 먼저 오름차순이나 내림차순으로 숫자 정렬
2. 가장 중앙에 있는 요소 두 개 더하고, 양쪽으로 나아가면서 두 개의 요소 더해 이전 두 개 더한 값과 비교
3. 그렇게 해서 나온 최종값이 각 그룹에 있는 원소의 합 중 최댓값이면서 모든 경우의 수 중 최댓값의 최솟값으로 나타낼 수 O
'''

# 그룹의 수
n = int(input())

# 그룹의 대상인 리스트의 요소 입력
arr = sorted(list(map(int, input().split())))
pre_sum_val = 0

# 처음에 중앙의 값들을 더하기 위해 인덱스 i, j 설정
i = len(arr) // 2 - 1
j = (len(arr) // 2)

while True:
    if i == -1 or j == len(arr) - 1: #만약 인덱스 i 가 0 아래에 있거나 인덱스 j가 리스트의 끝을 넘는다면 반복문 종료 후 pre_sum_val 출력
        break
    if i == len(arr) // 2 - 1:  # 맨 처음 pre_sum_val 설정하기 위해 정렬된 리스트의 가장 중앙 2개값을 더한 값으로 초기값 설정
        pre_sum_val = arr[i] + arr[j]
    else:   # 점차 arr[i]과 arr[j]가 양쪽으로 가면서 더하여 sum_val에 저장. pre_sum_val보다 크다면 갱신.
        sum_val = arr[i] + arr[j]
        if pre_sum_val < sum_val:
            pre_sum_val = sum_val
    
    # 양쪽으로 가기 위해 i 는 -1을, j는 +1을 더함
    i -= 1
    j += 1

print(pre_sum_val)