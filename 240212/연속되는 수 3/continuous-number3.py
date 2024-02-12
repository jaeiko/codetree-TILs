'''
시뮬레이션 II 문제

0이 아닌 N개의 숫자들이 주어졌을 때, 부호가 동일한 숫자로만 이루어진 연속 부분 수열 중 최대 길이를 구하는 프로그램
1 ≤ N ≤ 1,000
-1,000 ≤ 입력으로 주어지는 숫자 ≤ 1,000
'''

def check_signed(num):
    if num > 0:
        return 1
    elif num < 0:
        return 0

# n 입력
n = int(input())

cur_cnt = 1     # 현재 카운트하는 변수
max_cnt = 0     # 카운트 횟수가 최대인 값을 저장하는 변수
signed = 0      # 부호 확인용 변수(0 : 음수 / 1 : 양수)
for i in range(n):
    input_num = int(input())    # 숫자 입력
    if i == 0:  # 첫 번째로 들어온 숫자이면 현재 카운트는 1로 유지하고 그 숫자의 부호에 맞게 signed 변수에 저장
        signed = check_signed(input_num)
    else:       # 두 번째부터 들어오는 숫자는 여기에 해당
        if signed == check_signed(input_num):   # 이전 값의 부호와 현재값의 부호와 같다면 cur_cnt 1증가, 이 때 max_cnt 변수값를 넘었다면 max_cnt 변수의 최댓값 갱신
            cur_cnt += 1
            if max_cnt < cur_cnt:
                max_cnt = cur_cnt
        else:   # 부호가 다르다면 signed 변수 갱신 / cur_cnt는 1로 초기화
            signed = check_signed(input_num)
            cur_cnt = 1

# 출력
print(max_cnt)