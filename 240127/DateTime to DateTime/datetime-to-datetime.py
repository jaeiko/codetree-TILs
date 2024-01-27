'''
2011년 11월 11일 11시 11분에서 시작하여 2011년 11월 a일 b시 c분까지 몇 분이 걸리는지를 계산하는 프로그램
'''
import sys

# a, b, c 입력
a, b, c = tuple(map(int, input().split()))

# 일(day), 시(hour), 분(mins), 경과일(elapsed_mis) 초기화
day, hour, mins = 11, 11, 11
elapsed_mins = 0

while True:
    # a일 b시 c분이 11일 11시 11분보다 더 앞서다면 -1을 출력 후 종료
    if a < 11 or (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
        print(-1)
        sys.exit(0)
    
    # a일 b시 c분까지 왔으면 break
    if day == a and hour == b and mins == c:
        break
    
    # 분, 총 경과 시간(단위 : 분) 1 증가
    mins += 1
    elapsed_mins += 1

    # 만약 mins가 60분이 되었다면 hour 1 증가 / mins를 0으로 초기화
    if mins == 60:
        hour += 1
        mins = 0
        if hour == 24:   # 만약 hour이 24시간을 넘어갔다면 day를 1증가, hour를 0으로 초기화
            day += 1
            hour = 0

# break 후 총 걸린 시간(단위 : 분) 출력
print(elapsed_mins)