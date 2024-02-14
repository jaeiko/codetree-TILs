'''
시뮬레이션 II 문제

n개의 수로 이루어진 수열 정보와 정수 t가 주어졌을 때, t보다 큰 수로만 이루어진 연속 부분 수열 중 최대 길이를 구하는 프로그램을 작성
'''

# n, t 입력
n, t = tuple(map(int, input().split()))

# n개의 수 입력
arr = list(map(int, input().split()))

cnt = 0 # 현재 카운트하는 변수
max_cnt = 0 # 최대 카운트 변수

for i in range(n):
    if t < arr[i]:   # t보다 큰 수 일 때 cnt 1 증가 / max_cnt보다 cnt 값을 넘어섰다면 최댓값 갱신
        cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
    else:   # t 이하의 수라면 cnt 0으로 초기화
        cnt = 0

# 출력
print(max_cnt)