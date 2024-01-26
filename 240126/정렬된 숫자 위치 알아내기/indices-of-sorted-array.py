# 요소 개수 n
n = int(input())

# 요소 입력해서 nums 리스트에 저장
nums = list(map(int, input().split()))

# nums 리스트를 오름차순 정렬하여 sorted_nums 리스트에 저장
sorted_nums = sorted(nums)

# 인덱스 번호를 저장할 리스트
index_list = []

# 리스트 요소를 찾아갈 인덱스
i = 0
# nums 리스트의 요소가 들어있는 순서대로 반복문 실행
for elem in nums:
    index_list.append(sorted_nums.index(elem) + 1)  # 정렬된 리스트 sorted_nums의 해당 요소의 위치(index+1)를 index_list에 추가
    if index_list.count(elem) >= 2: # 만약 그 요소의 위치가 이미 index_list에 들어있다면
        index_list[i] += nums[0:i].count(elem) - 1 # 먼저 입력으로 주어진 원소가 더 앞으로 와야 하니 나중에 입력된 원소는 먼저 들어온 원소의 인덱스의 개수만큼 더해서 증가시킴.
    i += 1


# 출력
for elem in index_list:
    print(elem, end=' ')