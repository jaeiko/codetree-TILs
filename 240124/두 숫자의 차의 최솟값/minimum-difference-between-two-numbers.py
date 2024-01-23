n = int(input())
arr = list(map(int, input().split()))

min_val = arr[1] - arr[0]
for i in range(1, n):
    if i == n-1:
        break
    if arr[i+1] - arr[i] < min_val:
        min_val = arr[i+1] - arr[i]

print(min_val)