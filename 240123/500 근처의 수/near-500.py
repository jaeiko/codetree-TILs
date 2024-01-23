import sys
arr = list(map(int, input().split()))

# 500 미만의 수 중 가장 큰 수 찾는 변수
sub_val1 = abs(min(arr) - 500)
max_val = 0

# 500 미만의 수 중 가장 작은 수 찾는 변수
sub_val2 = abs(max(arr) - 500)
min_val = 0

for i in range(1, 10):
    if arr[i] - 500 < 0 and abs(arr[i] - 500) < sub_val1:  # 500 미만의 수 중 가장 큰 수 찾는 코드
        sub_val1 = abs(arr[i] - 500)
        max_val = arr[i]
    elif arr[i] - 500 > 0 and abs(arr[i] - 500) < sub_val2:  # 500 초과의 수 중 가장 작은 수를 찾는 코드
        sub_val2 = abs(arr[i] - 500)
        min_val = arr[i]

print(max_val, min_val)