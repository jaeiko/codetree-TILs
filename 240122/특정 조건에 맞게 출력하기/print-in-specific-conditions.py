arr = list(map(int, input().split()))

for elem in arr:
    if elem == 0:
        continue
    elif elem % 2 == 0:
        print(int(elem / 2), end=' ')
    else:
        print(elem + 3, end=' ')