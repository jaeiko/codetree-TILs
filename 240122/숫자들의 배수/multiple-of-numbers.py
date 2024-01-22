n = int(input())
i = 1
count = 0

arr = []

while True:
    arr.append(n * i)
    if (n * i) % 5 == 0:
        count += 1
        if count == 2:
            break
    i += 1

for elem in arr:
    print(elem, end=' ')