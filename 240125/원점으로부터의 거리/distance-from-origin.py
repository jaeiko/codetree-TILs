# 거리(distance)와 번호(i)를 가지고 있는 Coordinate 클래스
class Coordinate:
    def __init__(self, x, y, i):
        distance = abs(x-0) + abs(y-0)  # 멘하턴 거리
        self.distance = distance
        self.i = i

# 좌표 입력 횟수 n
n = int(input())

# 좌표 리스트
coordinate_list = []

for i in range(1, n+1):
    x, y = tuple(map(int, input().split())) # 좌표의 x, y 값 입력
    coordinate_list.append(Coordinate(x, y, i)) # 좌표의 x, y와 번호 i를 가진 Coordinate 객체 생성하여 좌표 리스트에 추가

# 원점에서 가까운 점부터 순서대로 / 만약 거리가 같으면 번호가 작은 점부터 순서대로 출력하도록 정렬
sorted_coordinate_list = sorted(coordinate_list, key=lambda x: (x.distance, x.i))

# 출력
for coordinate in sorted_coordinate_list:
    print(coordinate.i)