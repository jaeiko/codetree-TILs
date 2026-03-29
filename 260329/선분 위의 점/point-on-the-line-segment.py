n, m = map(int, input().split())    # n : 점 갯수 / m: 선분 갯수
dot = list(map(int, input().split()))
line = list()
max_value = 0
min_value = 10 ** 9

# Please write your code here.
for i in range(m):  # 선 정보 리스트에 담기
    x1, x2 = map(int, input().split())
    line.append((x1, x2))
    max_value = max(max_value, x2)  # 선분 x2 중 가장 큰 값을 max로
    min_value = min(min_value, x1)  # 선분 x1 중 가장 작은 값을 min으로

# # 이진탐색
# def binary_search(target, x1, x2):
#     left = x1
#     right = x2

#     while left <= right:
#         mid = (left + right) // 2
#         if mid == target:
#             return True
#         elif mid < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return False

        
# 해당 선분에서 점의 개수가 몇 개 들어있는지 체크
for i in range(m):
    count = 0
    for j in range(n):  # 각 선분마다 점이 몇개 들어있는지 체크
        if dot[j] < min_value or dot[j] > max_value:    # 애초에 점의 위치가 존재하는 선분의 범위보다 벗어나있으면 바로 생략
            continue
        if line[i][0] <= dot[j] and dot[j] <= line[i][1]:
            count += 1 

        # if binary_search(dot[j], line[i][0], line[i][1]):
        # count += 1
    
    # 결과 반환
    print(count)