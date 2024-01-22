n = int(input())
arr = list(map(int, input().split()))

# Step 1: 처음 2개의 원소 중 더 큰 값을 max1, 작은 값을 max2로 설정
if arr[0] > arr[1]:
    max1, max2 = arr[0], arr[1]
else:
    max2, max1 = arr[1], arr[0]

# Step 2: 3번째 원소부터 보면서 max1과 max2를 갱신
for i in range(2, n):
    if arr[i] > max1:
        max2, max1 = max1, arr[i]
    elif arr[i] > max2:
        max2 = arr[i]

print(max1, max2)