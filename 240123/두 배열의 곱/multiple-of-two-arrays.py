arr1 = [    # 행렬1
    list(map(int, input().split()))
    for _ in range(3)
]

n = input() # 엔터키 받는 용도(줄 간격)

arr2 = [    # 행렬2
    list(map(int, input().split()))
    for _ in range(3)
]

# 행렬1과 행렬2의 같은 위치에 있는 숫자의 곱을 출력
for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end=' ')
    print()