arr = list(map(int, input().split()))

sum = 0
count = 0
for elem in arr:
    if elem == 0:
        break
    if elem % 2 == 0:
        sum += elem
        count += 1

print(count, sum)