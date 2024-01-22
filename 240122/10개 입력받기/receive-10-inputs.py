arr = list(map(int, input().split()))

new_arr = []

for elem in arr:
    if(elem == 0):
        break
    new_arr.append(elem)

print(f'{sum(new_arr)} {sum(new_arr) / len(new_arr):.1f}')