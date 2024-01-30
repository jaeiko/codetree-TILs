# 명령 횟수 n 입력
n = int(input())

# 좌표 리스트
coordinates = []

# OFFSET 설정 (-100000 ~ 100000 => 0 ~ 200000)
OFFSET = 100000

# 현재 위치
cur = 0

for _ in range(n):
    x, command = tuple(map(str, input().split())) # x : 이동한 거리 / command : 방향

    x = int(x)

    if command == 'L':
        # 왼쪽으로 이동할 경우 : 현재 위치 - 이동한 거리
        section_left = (cur - x) + 1
        section_right = cur + 1
        cur = (cur - x) + 1    # 현재 위치는 왼쪽으로 x 간 크기만큼 이동(왼쪽은 (cur - x) + 1 부터 cur까지 타일 포함)
        color = 'W' # 왼쪽으로 이동하면서 왼쪽으로 뒤집음 => 흰색으로 바뀜
    else:
        # 오른쪽으로 이동할 경우 : 현재 위치 - 이동한 거리
        section_left = cur
        section_right = cur + x
        cur += x - 1    # 현재 위치는 오른쪽으로 x -1 간 크기만큼 이동(오른쪽은 cur 부터 cur + (x-1)까지 타일 포함)
        color = 'B' # 오른쪽으로 이동하면서 오른쪽으로 뒤집음 => 검정색으로 바뀜

    coordinates.append([section_left, section_right, color])   # 왼쪽 위치와 오른쪽 위치(즉, 이동한 거리) 그리고 색깔을 좌표 리스트에 저장

checked = [''] * 200001 # 200001개의 회색 타일

for x1, x2, color in coordinates:
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    if x1 == x2:
        checked[x1] = color

    # 구간 칠하기(구간 단위이므로 x2에 등호 들어가지 않음을 주의)
    for i in range(x1, x2):
        checked[i] = color

white_cnt = 0   # 흰색 타일 갯수
black_cnt = 0   # 검은색 타일 개수

# 흰색 타일이면 white_cnt에 1증가, 검은색 타일이면 black_cnt에 1증가
for elem in checked:
    if elem == 'W':
        white_cnt += 1
    elif elem == 'B':
        black_cnt += 1

# 출력
print(white_cnt, black_cnt)