class Student:
    def __init__(self, cm, kg, pid):
        self.cm = cm    # 키
        self.kg = kg    # 몸무게
        self.pid = pid  # 번호

students = []

# 들어갈 학생 데이터의 개수
n = int(input())

pid = 1 # 학생 번호 부여


for _ in range(n):
    cm, kg = list(map(int, input().split()))    # 학생의 키, 몸무게 입력
    students.append(Student(cm, kg, pid))       # 학생의 키, 몸무게, 번호 객체를 students 리스트에 추가
    pid += 1    # 번호 1 증가

# 키가 더 큰 학생이 앞으로 / 만약 키가 동일하다면 몸무게가 더 큰 학생이 앞으로 / 키, 몸무게 다 동일하다면 번호가 작은 학생이 앞으로
students.sort(key=lambda x: (-x.cm, -x.kg, pid))

# 정렬 이후 학생 정보 출력
for student in students:
    print(student.cm, student.kg, student.pid)