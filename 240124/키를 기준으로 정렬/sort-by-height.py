# 이름, 키, 몸무게를 가지고 있는 PeopleInfo 클래스
class PeopleInfo:
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

n = int(input())    # 사람 입력 횟수 입력

peoples = []    # PeopleInfo 객체들을 담는 리스트

# n만큼 반복문 실행
for _ in range(n):
    name, cm, kg = tuple(map(str, input().split())) # 한 사람의 이름, 키, 몸무게 입력
    peoples.append(PeopleInfo(name, int(cm), int(kg)))  # 이름, 키, 몸무게를 가진 PeopleInfo 객체 만들어 peoples 리스트에 추가

peoples.sort(key=lambda x: x.cm) # 키 기준 오름차순 정렬

for people in peoples: # 정렬 이후의 결과 출력
    print(people.name, people.cm, people.kg)