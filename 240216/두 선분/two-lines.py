'''
케이스별로 나누기 - 겹치는 경우

두 선분의 교차 여부를 판단하는 프로그램
'''

# (x1, x2) , (x3, x4) 입력
x1, x2, x3, x4 = tuple(map(int, input().split()))

if x4 < x1 or x2 < x3:  # 두 선분이 안 겹치면 nonintersecting 출력
    print('nonintersecting')
else:
    print('intersecting')   # 두 선분이 겹치면 intersecting 출력