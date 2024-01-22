max_val = 0

arr = list(map(int, input().split()))
for elem in arr:
    if max_val < elem:
        max_val = elem

print(max_val)