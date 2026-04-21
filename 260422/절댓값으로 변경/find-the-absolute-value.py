n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def absolute_val(arr):
    for num in arr:
        if num < 0:
            print(num - num * 2, end=' ')
        else:
            print(num, end=' ')

absolute_val(arr)