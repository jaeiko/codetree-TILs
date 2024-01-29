'''
위치 0에서 시작하여 n번의 명령에 걸쳐 움직인 뒤, 2번 이상 지나간 영역의 크기를 출력하는 프로그램
'''

# 명령 횟수 n 입력
n = int(input())

# 좌표 리스트
coordinates = []

# OFFSET 설정 (-1000~1000 => 0~2000)
OFFSET = 1000

# 현재 위치
cur = 0

for _ in range(n):
    x, command = tuple(map(str, input().split()))   # x : 이동한 거리 / command : 방향
    x = int(x)

    if command == 'L':
        # 왼쪽으로 이동할 경우 : 현재 위치 - 이동한 거리
        section_left = cur - x
        section_right = cur
        cur -= x
    else:
        # 오른쪽으로 이동할 경우 : 현재위치 + 이동한 거리
        section_left = cur
        section_right = cur + x
        cur += x
    
    coordinates.append([section_left, section_right])   # 왼쪽 위치와 오른쪽 위치(이동한 거리)를 좌표 리스트에 저장

checked = [0] * 2001    # 2001개의 구간을 가진 수직선 (명령은 총 100번, 한번에 이동하는 거리는 최대 10까지이므로)

for x1, x2 in coordinates:
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    
    # 구간 칠하기(구간 단위이므로 x2에 등호 들어가지 않음에 주의)
    for i in range(x1, x2):
        checked[i] += 1

# 2번 이상 지나간 영역의 크기 구하기
count = 0
for elem in checked:
    if elem >= 2:
        count += 1

# 출력
print(count)