import sys

# 입력 속도 최적화
input = sys.stdin.readline
n = int(input())
k = int(input())

lo = 1
# 최적화 1: K번째 수는 K를 넘을 수 없으므로 탐색 상한선을 k로 설정
hi = k 
ans = k

while lo <= hi:
    mid = (lo + hi) // 2
    
    val = 0
    # 최적화 2: i가 mid보다 크면 몫이 0이므로, min(n, mid)까지만 순회
    for i in range(1, min(n, mid) + 1):
        val += min(n, mid // i)
    
    if val >= k:
        hi = mid - 1
        ans = min(ans, mid)
    else:
        lo = mid + 1

print(ans)