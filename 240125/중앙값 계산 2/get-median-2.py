# 입력할 요소 개수 n 입력
n = int(input())

# 요소 입력해서 arr 리스트에 저장
arr = list(map(int, input().split()))

for i in range(n):
    if (i+1) % 2 != 0:  # 홀수 번째 수 일 때
        sorted_arr = sorted(arr[0:i+1])    # 중앙값을 구하기 위해 0 ~ i번째 요소들을 오름차순으로 정렬하여 sorted_arr 에 저장
        print(sorted_arr[i // 2], end=' ') # 중앙값 출력