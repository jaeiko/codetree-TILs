# 이름, 국어/영어/수학 점수를 가진 student 클래스
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = []
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append(Student(name, int(kor), int(eng), int(math)))   # 학생 객체를 리스트에 추가

# 먼저 국어 내림차순 정렬, 만약 동점이라면 영어 내림차순 정렬, 그래도 동점이라면 수학 내림차순 정렬
students.sort(key=lambda x: (x.kor + x.eng + x.math))

# 출력
for student in students:
    print(student.name, student.kor, student.eng, student.math)