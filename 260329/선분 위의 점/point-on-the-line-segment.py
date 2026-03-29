# 그냥 무작정 조건식으로 찾는건 이중반복문 써야 하는데 시간 초과 걸리니 다른 방식을 사용하자!
n, m = map(int, input().split())
dot = list(map(int, input().split()))

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid  # target 이상이면 일단 후보로 두고 왼쪽 탐색
        else:
            left = mid + 1
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid  # target 초과면 일단 후보로 두고 왼쪽 탐색
        else:
            left = mid + 1
    return left

dot.sort()

for i in range(m):
    x1, x2 = map(int, input().split())
    # 선분 [x1, x2]에 포함된 점의 개수 = x2 초과인 첫 위치 - x1 이상인 첫 위치
    count = upper_bound(dot, x2) - lower_bound(dot, x1)
    print(count)