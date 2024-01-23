n = int(input())

price_arr = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    difference = price_arr[1] - price_arr[0]
    for i in range(n):
        for j in range(i + 1, n):
            if j == n:
                break
            if price_arr[j] - price_arr[i] > difference:
                difference = price_arr[j] - price_arr[i]
    print(difference)