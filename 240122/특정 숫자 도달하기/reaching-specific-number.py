arr = list(map(int, input().split()))

sum = 0
length = 0
for elem in arr:
    if(elem >= 250):
        break
    sum += elem
    length += 1

print(f"{sum} {sum / length:.1f}")