import sys

# 입력 속도 최적화
input = sys.stdin.readline
n = int(input())    # n*n 크기 배열
k = int(input())    # K번째 오는 수 찾기

lo = 1
# 최적화 1: K번째 수는 K를 넘을 수 없으므로 탐색 상한선을 k로 설정
hi = k 
ans = k

while lo <= hi:
    mid = (lo + hi) // 2
    
    val = 0

    # mid값보다 작은 값들의 개수 구하기
    # 최적화 2: 어차피 i가 mid보다 크면 몫이 0이라서 0을 더하건 말건 의미가 없으므로, min(n, mid)까지만 순회
    for i in range(1, min(n, mid) + 1):
        # i행에 올수 있는 숫자는 i, 2i, 3i, ... 등 i의 배수들
        # 이 때 i번째 행에 적혀있는 숫자 중 임의의 mid값보다 같거나 작은 숫자의 개수는 M/i
        # 그 이유는 pi <= M(p=1,2,3...) -> p <= M/i 가 되기 때문
        # 이 때, 이 문제에서는 n * n 행렬이기 때문에 p <= n이다.
        # 따라서 val에 각 행에 대해 M이하인 수의 개수인 min(n, mid/i)를 전부 더하는 것이 핵심
        val += min(n, mid // i)
    
    if val >= k:    # 만약 인덱스 값 val이 우리가 찾고자 하는 인덱스 값 k보다 같거나 크다면
        hi = mid - 1    # 혹시나 그 이전에 조건을 만족하는 k가 있을 수 있으니 hi값 갱신
        ans = min(ans, mid) # 그러면서 일단 해당 val 인덱스인 mid값을 답으로 갱신
    else:
        lo = mid + 1

print(ans)