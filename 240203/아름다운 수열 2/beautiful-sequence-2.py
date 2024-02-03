'''
완전탐색 문제

수열 A에서 길이가 M인 연속 부분 수열들 중 아름다운 수열의 수를 세는 프로그램
아름다운 수열 : 수열 B의 각 원소들의 순서를 바꿔 나오는 수열
'''
# 수열 a의 길이 n과 수열 b의 길이 m 입력
n, m = tuple(map(int, input().split()))

# 수열 a, 수열 b 입력
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 완전탐색 - 이 때 a의 일부분(b의 크기만큼)을 오름차순 정렬한 값이 b을 오름차순 정렬한 값과 같으면 카운트(사실상 정렬 안했을 때의 값과 아름다운 수열의 값이랑 일치하므로)
cnt = 0
for i in range(n-m+1):
    if sorted(a[i:i+m]) == sorted(b):
        cnt += 1

# 출력
print(cnt)