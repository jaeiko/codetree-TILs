N = int(input())

arr = list(map(int, input().split()))

for i in range(N):
    for j in range(i + 1, N):
        if arr[i] < arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        
print(arr[0], arr[1])