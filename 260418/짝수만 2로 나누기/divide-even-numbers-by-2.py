n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def modify(arr):
    for i in arr:
        if i % 2 == 0:
            print(int(i / 2), end=" ")
        else:
            print(i, end=" ")

modify(arr[:])