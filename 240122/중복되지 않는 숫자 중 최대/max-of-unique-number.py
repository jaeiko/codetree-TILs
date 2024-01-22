N = int(input())

arr = list(map(int, input().split()))

max_num = -1
for i in range(N):
    if max_num <= arr[i]:
        if arr.count(arr[i]) > 1:
            max_num = -1
            continue
        max_num = arr[i]

print(max_num)