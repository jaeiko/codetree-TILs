class PeopleInfo:
    def __init__(self, name, addr, city):
        self.name = name    # 이름
        self.name = addr    # 번지수
        self.city = city    # 지역

n = int(input())

# 사람 리스트
people_list = []

for i in range(n):
    name, addr, city = list(map(str, input().split()))  # 이름, 번지수, 지역 입력
    people_list.append(PeopleInfo(name, addr, city))    # 사람 리스트에 이름, 번지수, 지역 추가
    if i == 0: # 0번 인덱스의 이름, 번지수, 지역으로 초기값 설정
        compare_name = name
        compare_addr = addr
        compare_city = city
        continue
    else:      # compare_name 보다 더 사전순으로 느린 사람 있으면 compare_name, compare_addr, compare_city 변경
        if name > compare_name:
            compare_name = name
            compare_addr = addr
            compare_city = city

# 사전순으로 이름이 가장 느린 사람의 자료를 출력
print(f'name {compare_name}')
print(f'addr {compare_addr}')
print(f'city {compare_city}')