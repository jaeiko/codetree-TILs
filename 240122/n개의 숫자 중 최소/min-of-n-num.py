import sys

_ = int(input())
min_val = sys.maxsize   # sys.maxsize 이용해 초기값 설정
arr = list(map(int, input().split()))

for elem in arr:
    if min_val > elem:
        min_val = elem

print(min_val, arr.count(min_val))