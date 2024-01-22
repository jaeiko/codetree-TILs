arr = list(map(int, input().split()))

reversed_arr = arr[::-1]


for i in range(len(reversed_arr)):
    if(i == 0 and reversed_arr[i] == 0):
        continue
    else:
        if(reversed_arr[i] == 0):
            break
        print(reversed_arr[i], end=' ')