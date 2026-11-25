n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
print(*(sorted(nums)))
print(*reversed(sorted(nums)))