'''
2024년 m1월 d1일이 월요일 이었다면, 2024년 m2월 d2까지 A 요일은 몇 번 등장하는지 구하는 프로그램
'''

# m1, d1, m2, d2 입력
m1, d1, m2, d2 = tuple(map(int, input().split()))
# 요일 입력
day_of_the_week = input()

# 해당 요일의 총 등장 횟수(checked)
checked = 0

# 만약 찾고자 하는 요일이 월요일이면 시작하는 하루도 체킹되어야 하므로 checked에 1 증가
if day_of_the_week == 'Mon':
    checked += 1

# 각 달의 마지막 날 1. 2.  3.  4.  5.  6.  7.  8.  9.  10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 요일 리스트(day_of_the_weeks) 와 요일 리스트를 이용할 인덱스(i)
day_of_the_weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
i = 0   # 2024년 m1월 d1일이 월요일로 가정한다고 했으므로 인덱스는 0부터 시작

while True:
    if m1 == m2 and d1 == d2:   # 반복문 돌리면서 어느 순간 m2와 d2까지 갔다면 break
        break;

    d1 += 1     # 하루 증가
    i += 1      # i 증가(다음 요일로)
    if i == 7:  # 만약 i 가 7이라면 day_of_the_weeks 리스트에서 다시 월요일인 0번으로 가야하니 i = 0으로 초기화
        i = 0
    
    # 현재 i가 day_of_the_weeks 리스트에서 우리가 찾고자 하는 요일(day_of_the_week)의 인덱스에 해당하면 checked는 1증가
    if i == day_of_the_weeks.index(day_of_the_week):
        checked += 1

    # d1(일)이 해당 달의 마지막 날을 넘어갔다면 m1(월)은 한 달 증가, d1(일)은 다시 1일로 초기화
    if d1 > num_of_days[m1]:
        m1 += 1
        d1 = 1
    

# break 후 총 A 요일 몇 번 등장했는지 출력
print(checked)