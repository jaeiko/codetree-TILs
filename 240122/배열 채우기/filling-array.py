arr = list(map(int, input().split()))

new_arr = []

for elem in arr:
    if(elem == 0):
        break
    new_arr.append(elem)

for elem in new_arr[::-1]:
    print(elem, end=' ')