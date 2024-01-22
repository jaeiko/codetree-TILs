arr = list(map(int, input().split()))
new_arr = []
if 999 in arr and -999 in arr:
    if arr.index(999) > arr.index(-999):
        new_arr = arr[0:arr.index(-999)]
    else:
        new_arr = arr[0:arr.index(999)]
elif 999 in arr:
    new_arr = arr[0:arr.index(999)]
elif -999 in arr:
    new_arr = arr[0:arr.index(-999)]

max_val = 0
min_val = 0
for elem in new_arr:
    if max_val < elem:
        max_val = elem
    elif min_val > elem:
        min_val = elem

print(max_val, min_val)