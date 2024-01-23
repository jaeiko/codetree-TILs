n = int(input())
arr = list(map(int, input().split()))
index_arr = list()

i = 1
while True:
    index_arr.append(arr.index(max(arr)) + 1)
    if arr.index(max(arr)) == 0:
        break
    arr = arr[arr.index(max(arr))-i::-1]
    i += 1



for elem in set(index_arr):
    print(elem, end=' ')