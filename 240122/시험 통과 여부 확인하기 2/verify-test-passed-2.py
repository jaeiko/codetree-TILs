n = int(input())

count = 0
for i in range(n):
    sum = 0
    arr = list(map(int, input().split()))
    for elem in arr:
        sum += elem
    if sum / 4 >= 60:
        print('pass')
        count += 1
    elif sum / 4 < 60:
        print('fail')
print(count)