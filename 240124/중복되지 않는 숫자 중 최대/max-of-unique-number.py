N = int(input())

arr = sorted(list(map(int, input().split())), reverse=True)

max_num = -1
for i in range(N):
    if max_num <= arr[i]:
        if arr.count(arr[i]) > 1:
            max_num = -1
            continue
        max_num = arr[i]

print(max_num)