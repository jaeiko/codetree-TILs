# 키(cm), 몸무게(kg), 번호(i)를 가지고 있는 Student 클래스
class Student:
    def __init__(self, cm, kg, i):
        self.cm = cm
        self.kg = kg
        self.i =i

# 학생의 수 n
n = int(input())

# 학생 리스트
students = []

# 학생 개인의 키와 몸무게 입력 후 번호랑 같이 Student 객체에 저장 -> students 리스트에 추가
for i in range(1, n+1):
    cm, kg = tuple(map(int, input().split()))
    students.append(Student(cm, kg, i))

# 키가 더 작은 학생이 앞으로(키를 기준으로 오름차순)
# 키가 동일하다면, 몸무게가 더 큰 학생이 앞으로(몸무게를 기준으로 내림차순)
students.sort(key=lambda x:(x.cm, -x.kg))

# 학생 개개인의 키, 몸무게 출력
for student in students:
    print(student.cm, student.kg, student.i)