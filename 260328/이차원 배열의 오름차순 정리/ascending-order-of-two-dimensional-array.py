n = int(input())
k = int(input())

# Please write your code here.
lo = 1
hi = n*n
ans = n*n

while lo <= hi:
    mid = (lo + hi) // 2

    val = 0
    for i in range(1, n + 1):   # key point
        val += min(n, mid // i)
    
    if val >= k: # 현재 구한 val이 우리가 찾고자 하는 k보다 크거나 같은경우
        hi = mid - 1    # 답을 일단 정하고, 이 답보다 그 이전을 만족하는 값도 존재할 수 있으니 hi 조정
        ans = min(ans, mid)
    else:
        lo = mid + 1

print(ans)