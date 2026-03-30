import sys

M = int(input())

A, B = map(int, input().split())

min_count = sys.maxsize
max_count = -sys.maxsize

def binary_search(target):
    left, right = 1, M
    count = 0

    while left <= right:
        mid = (left + right) // 2
        count += 1

        if target == mid:
            return count
        elif target < mid:
            right = mid - 1
        else:
            left = mid + 1

count = 0
for i in range(A, B+1):
    target = i
    
    count = binary_search(target)

    min_count = min(min_count, count)
    max_count = max(max_count, count)

    
print(min_count, max_count)