'''
위치 0에서 시작하여 n번의 명령에 걸쳐 움직인 뒤, 2번 이상 지나간 영역의 크기를 출력하는 프로그램

이 문제의 포인트 : 결국 왼쪽으로 간 애들을을 이어서 만들고, 오른쪽으로 간 애들을 이어서 둘 다 0 부터 시작할 때 겹치는 구간이랑 같게 된다.
'''

# 명령 횟수 n 입력
n = int(input())

# 길이 1000까지의 구간(n * x의 최댓값은 1000이므로)
sections = [0] * 50

left_index = 0  # 왼쪽 인덱스
right_index = 0 # 오른쪽 인덱스

for _ in range(n):
    x, command = tuple(map(str, input().split()))   # 명령 입력

    if command == 'L':      # 왼쪽 이동이면 이전에 왼쪽으로 갔던 곳부터 시작해서 구간을 지나간다.
        for i in range(left_index, left_index + int(x)):
            sections[i] += 1
        left_index += int(x)    # left_index에 x+1만큼 증가
    elif command == 'R':    # 오른쪽 이동이면 이전에 오른쪽으로 갔던 곳부터 시작해서 구간을 지나간다.
        for i in range(right_index, right_index + int(x)):
            sections[i] += 1
        right_index += int(x)   # right_index에 x+1만큼 증가

# 2번 이상 지나간 구간 구하기
checked = 0
for section in sections:
    if section >= 2:
        checked += 1

# 출력
print(checked)