_ = int(input())
arr = list(map(int, input().split()))

even_arr = [elem for elem in arr if elem % 2 == 0]

for elem in even_arr:
    print(elem, end=' ')