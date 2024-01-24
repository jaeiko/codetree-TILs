n, k = list(map(int, input().split()))  # n : 리스트 요소 개수 / k : 리스트에서 찾을 요소 인덱스

arr = list(map(int, input().split()))   # 리스트 입력

arr.sort()  # arr 리스트 오름차순

print(arr[k-1])