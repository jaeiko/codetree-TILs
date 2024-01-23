arr = [
    list(map(str, input().split()))
    for _ in range(5)
]

for i in range(len(arr)):
    for elem in arr[i]:
        print(elem.upper(), end=' ')
    print()