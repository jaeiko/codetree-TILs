n, m = map(int, input().split())

# Please write your code here.
def swap(a, b):
    temp = a
    a = b
    b = temp

    print(a, b)

swap(n, m)