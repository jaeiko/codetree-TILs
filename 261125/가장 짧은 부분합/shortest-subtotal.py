def sliding_window_min_length(arr, target_sum):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target_sum and left <= right:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else -1


# 원소 N개, 합 S이상
n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
print(sliding_window_min_length(arr, s))