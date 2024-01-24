n = int(input())
arr = list(map(int, input().split()))

sort_list = sorted(arr)
reversed_sort_list = sorted(arr, reverse=True)

for elem in sort_list:
    print(elem, end=' ')

print()

for elem in reversed_sort_list:
    print(elem, end=' ')