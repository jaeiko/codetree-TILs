"""
2011년 m1월 d1일로부터 2011년 m2월 d2일까지는 총 며칠이 있는지를 계산하는 프로그램
"""

# m1, d1, m2, d2 입력
m1, d1, m2, d2 = tuple(map(int, input().split()))

# 월, 일 변수
month, day = m1, d1
elapsed_days = 0    # 총 일수 저장하는 변수

                # 월별 마지막날 저장한 리스트
                  #1. 2.  3.  4.  5.  6.  7.  8.  9.  10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if month == m2 and day == d2:   # month, day가 m2, d2까지 왔으면 break
        break

    # 하루 지났으니 총 일수와 일을 1 증가시킴
    elapsed_days += 1
    day += 1

    # 해당 달의 day를 넘겼으면 month에 1증가, day를 0으로 초기화
    if day > num_of_days[month]:
        month += 1
        day = 0

# break 후 총 걸린 일수 출력
print(elapsed_days)