n, m = list(map(int, input().split()))

arr1 = [    # 행렬1
    list(map(int, input().split()))
    for _ in range(n)
]

arr2 = [    # 행렬2
    list(map(int, input().split()))
    for _ in range(n)
]

# 행렬1과 행렬2의 같은 위치에 있는 숫자의 곱을 출력
for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()