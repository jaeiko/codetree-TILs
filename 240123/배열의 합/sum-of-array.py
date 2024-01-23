arr = [
    list(map(int, input().split()))
    for _ in range(4)
]

for i in range(len(arr)):
    print(sum(arr[i]))