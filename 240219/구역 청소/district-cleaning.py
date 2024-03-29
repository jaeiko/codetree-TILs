'''
케이스별로 나누기 - 겹치는 경우

A, B는 1차원 수직선 상에서 구역 청소를 진행하려고 합니다.
A는 x = a 구역에서 x = b 구역 이내에서만 청소를 진행하고, B는 x = c 구역에서 x = d 구역 이내에서만 청소를 진행한다고 합니다. 
총 몇 구역이나 청소가 될지를 계산하는 프로그램을 작성해보세요. 단, A, B가 청소하는 구역은 겹칠 수 있음에 유의합니다.
'''

# a, b 입력
a, b = tuple(map(int, input().split()))

# c, d 입력
c, d = tuple(map(int, input().split()))

# 0을 a, b, c, d 중 최댓값만큼 가진 리스트 생성
arr = [0] * max(a, b, c, d)

# 구간을 지점으로 생각하면 된다.
# a ~ (b-1) 구간까지 청소(청소한 구역을 1로 표시)
for i in range(a, b):
    arr[i] = 1

# c ~ (d-1) 구간까지 청소(청소한 구역을 1로 표시)
for i in range(c, d):
    arr[i] = 1

# 청소한 구역 칸수 출력
print(arr.count(1))