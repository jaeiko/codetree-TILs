'''
값을 반환하지 않는 함수 문제

 별 10개를 찍는 것을 5번 반복하는 프로그램
'''
# 별 10개를 출력하는 함수
def print_10_stars():
    print("*" * 10)

# 반복문을 통하여 50개의 별 출력
for _ in range(5):
    print_10_stars()