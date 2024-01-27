'''
2011년 11월 11일 a시 b분
~
2011년 11월 11일 c시 d분
까지 총 걸린 시간 계산하는 프로그램
'''
a, b, c, d = tuple(map(int, input().split()))
hour, mins = a, b
elapsed_time = 0

while True:
    if hour == c and mins == d:     # 해당 시간대 타임까지 도달했으면 break
        break

    elapsed_time += 1   # 총 소요시간 1 증가(단위 : 분)
    mins += 1   # 분 1 증가

    if mins == 60:  # 60분이 되었으면 hour 는 1 증가, mins 는 다시 0으로 초기화
        hour += 1
        mins = 0

# break 후 elapsed_time 출력
print(elapsed_time)