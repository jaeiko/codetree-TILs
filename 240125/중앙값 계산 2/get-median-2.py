# 입력할 요소 개수 n 입력
n = int(input())

# 요소 입력해서 정렬한 뒤, arr 리스트에 저장(중앙값 찾기 위해 미리 오름차순으로 정렬)
arr = sorted(list(map(int, input().split())))

for i in range(n):
    if (i+1) % 2 != 0:  # 홀수 번째 수 일 때
        print(arr[i // 2], end=' ') # 중앙값 출력