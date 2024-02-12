'''
시뮬레이션 II 문제

N개의 숫자들이 주어졌을 때, 증가하는 연속 부분 수열 중 최대 길이를 구하는 프로그램
증가하는 연속 부분 수열 : 연속 부분 수열 중 원소의 숫자가 계속 커지는 수열
'''

# n 입력
n = int(input())

# cnt : count 변수 / max_cnt : 연속 부분 수열 중 최대 길이
cnt, max_cnt = 1, 1
pre_num = 0 # 이전 숫자

for i in range(n):
    input_num = int(input())
    if i == 0:
        pre_num = input_num
    elif input_num - pre_num > 0:  # 들어온 숫자가 증가하는 연속 부분 수열을 만족하면 cnt 1 증가, 만약 cnt가 max_cnt를 넘어섰다면 최댓값 갱신
        cnt += 1
        pre_num = input_num
        if cnt > max_cnt:
            max_cnt = cnt
    else:   # 그 외 다른 숫자가 들어왔으면 cnt는 1로 초기화
        cnt = 1
        pre_num = input_num

# 출력
print(max_cnt)