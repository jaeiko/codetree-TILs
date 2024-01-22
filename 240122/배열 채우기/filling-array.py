arr = list(map(int, input().split()))

reversed_arr = []

i = 0
for elem in arr[::-1]:
    if(i == 0 and elem == 0):
        continue
    elif(elem == 0):
        break
    reversed_arr.append(elem)
    i += 1

for elem in reversed_arr:
    print(elem, end=' ')