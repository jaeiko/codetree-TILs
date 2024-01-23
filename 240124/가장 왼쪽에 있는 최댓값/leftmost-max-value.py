n = int(input())
arr = list(map(int, input().split()))
index_arr = list()

for elem in arr[arr.index(max(arr))::-1]:
    index_arr.append(arr.index(elem) + 1)

for elem in set(index_arr):
    print(elem, end=' ')