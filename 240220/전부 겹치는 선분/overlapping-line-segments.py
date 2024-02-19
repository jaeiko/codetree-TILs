'''
케이스별로 나누기 - 겹치는 경우

1차원 직선 상에 n개의 선분이 놓여 있을 때 모든 선분이 겹치는 지점이 있는지를 판단하는 프로그램
'''
import sys

arr = [0] * 101 # 총 100개의 선분

n = int(input())    # 선분의 개수 n 입력

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))   # x1, x2 입력
    for i in range(x1, x2+1):   # x1~x2까지의 선분이 놓여져 있는걸 arr에 1 증가로 표기
        arr[i] += 1

for element in arr:
    if element >= n:    # arr 리스트에서 요소 n이 발견되었으면 선분이 한 지점에서 모두 겹치므로 'Yes' 출력 후 프로그램 종료
        print('Yes')
        sys.exit(0)

print('No')    # arr 리스트에서 요소 n이 발견되지 않았으면 선분 모두 겹치지 않으므로 'No' 출력