arr = list(map(int, input().split()))

if(arr.index(0)):
    reversed_arr = arr[arr.index(0)-1::-1]
else:
    reversed_arr = arr[::-1]

for elem in reversed_arr:
    print(elem, end=' ')