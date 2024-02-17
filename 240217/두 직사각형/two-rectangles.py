import sys

'''
케이스별로 나누기 - 겹치는 경우

2차 평면 상에 두 직사각형이 주어졌을 때, 두 직사각형의 겹쳐져 있는지를 판단하는 프로그램
'''


# (x1, y1), (x2, y2) 값을 공백에 사이를 두고 입력
x1, y1, x2, y2 = tuple(map(int, input().split()))

# (a1, b1), (a2, b2) 값을 공백에 사이를 두고 입력
a1, b1, a2, b2 = tuple(map(int, input().split()))

# 두 사각형이 겹치지 않으면 "nonoverlapping" 출력 후 종료
if x2 <= a1 or a2 <= x1:
    if b2 <= y1 or y2 <= b1:
        print("nonoverlapping")
        sys.exit(0)

# 두 사각형이 겹친다면 "overlapping" 출력 후 종료
print("overlapping")