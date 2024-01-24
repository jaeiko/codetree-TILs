# Student 클래스
class Student:
    def __init__(self, name, cm, kg):
        self.name = name# 이름
        self.cm = cm    # 키
        self.kg = kg    # 몸무게

# Students 객체를 담을 students 리스트
students = []

# 학생 정보 5회 입력
for _ in range(5):
    name, cm, kg = list(map(str, input().split()))    # 학생의 이름, 키, 몸무게 입력
    students.append(Student(name, int(cm), float(kg)))       # 학생의 이름, 키, 몸무게를 담은 객체를 students 리스트에 추가

# 이름순으로 정렬
students.sort(key=lambda x: (x.name))
# 정렬 이후 학생 정보 출력
print('name')
for student in students:
    print(student.name, student.cm, student.kg)

print()

# 몸무게가 큰 순으로 정렬
print('height')
students.sort(key=lambda x: -(x.cm))
# 정렬 이후 학생 정보 출력
for student in students:
    print(student.name, student.cm, student.kg)