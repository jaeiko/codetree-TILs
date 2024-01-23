# 숫자, 리스트에 넣을 정수 입력
n = int(input())
arr = list(map(int, input().split()))

# 인덱스 값 넣을 리스트
index_arr = list()

while True:
    index_arr.append(arr.index(max(arr)) + 1)   # 리스트 중 가장 최댓값 인덱스 입력
    if arr.index(max(arr)) == 0:    # 그 최댓값 인덱스가 0이면 다 찾은거니 탈출
        break
    arr = arr[0:arr.index(max(arr))]    # 인덱스 0~최댓값 있는 인덱스-1까지의 리스트를 arr에 저장

# 요소 출력
for elem in index_arr:
    print(elem, end=' ')