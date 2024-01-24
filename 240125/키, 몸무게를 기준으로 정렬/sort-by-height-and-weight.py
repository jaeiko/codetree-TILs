# Student 클래스
class Student:
    def __init__(self, name, cm, kg):
        self.name = name# 이름
        self.cm = cm    # 키
        self.kg = kg    # 몸무게

n = int(input()
)
# Students 객체를 담을 students 리스트
students = []

# 학생 정보 n회 입력
for _ in range(n):
    name, cm, kg = list(map(str, input().split()))    # 학생의 이름, 키, 몸무게 입력
    students.append(Student(name, int(cm), int(kg)))       # 학생의 이름, 키, 몸무게를 담은 객체를 students 리스트에 추가

# 키를 기준으로 오름차순 정렬 / 키가 동일한 경우에는 모무게가 더 큰 사람이 먼저 나오도록 정렬
students.sort(key=lambda x: (x.cm, -x.kg))
# 정렬 이후 학생 정보 출력
for student in students:
    print(student.name, student.cm, student.kg)