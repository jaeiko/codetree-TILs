n, m = list(map(int, input().split()))

arr = [
    [0 for i in range(m)]
    for j in range(n)
]

val = 1
for i in range(n):
    for j in range(m):
        arr[i][j] += val
        val += 1

for row in arr:
    for elem in row:
        print(elem, end=' ') 
    print()