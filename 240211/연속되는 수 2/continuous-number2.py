'''
시뮬레이션 II 문제

N개의 숫자들이 주어졌을 때, 연속하여 동일한 숫자가 나오는 횟수 중 최대를 구하는 프로그램
'''

# n 입력
n = int(input())

pre_num = 0 # 이전 숫자 저장하는 변수
max_cnt = 0 # 연속하여 동일한 숫자가 나오는 횟수 중 최댓값을 저장하는 변수
cnt = 0 # 현재 연속하여 동일한 숫자가 나오는 횟수를 저장하는 변수

for i in range(n):
    input_num = int(input())    # 숫자 입력
    if i == 0 or pre_num == input_num:  # 첫 번째 경우이거나 이전 숫자와 들어온 숫자가 같다면 cnt 1 증가
        cnt += 1
        if max_cnt < cnt:   # 만약 cnt가 max_cnt를 넘어섰다면 최댓값 갱신
            max_cnt = cnt
    pre_num = input_num # 들어온 숫자는 이전 숫자에 저장

# 출력
print(cnt)