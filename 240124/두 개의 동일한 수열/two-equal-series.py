import sys

# 한 리스트당 몇 개의 원소를 입력할 것인지 정수 n 입력
n = int(input())

# 2개의 리스트 요소 입력 후 정렬해서 저장
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))

while True:
    for i in range(n):
        if arr1[i] != arr2[i]:  # 오름차순 정렬된 요소의 같은 인덱스끼리 비교하여 다르면 No 출력 후 종료
            print('No')
            sys.exit(0)
    break   # 위의 조건문에서 안걸리고 잘 통과되면 break 후 Yes 출력(동일한 리스트임이 검증되었으니)
    
print('Yes')