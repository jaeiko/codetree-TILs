import sys

a, b, c = map(int, input().split())

# Please write your code here.
def find_min(a, b, c):
    min_value = sys.maxsize
    if min_value > a:
        min_value = a
    if min_value > b:
        min_value = b
    if min_value > c:
        min_value = c

    return min_value

print(find_min(a, b, c))