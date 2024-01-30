'''
dx, dy 테크닉을 활용한 문제 3

숫자 0과 1로만 이루어진 n * n 크기의 격자 상태가 주어졌을 때,
각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수를 세는 프로그램
'''

# 범위 내에 있는지 확인하는 함수
def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

# 배열 크기 설정
n = int(input())

# 배열 입력(n * n)
arr = [
        list(map(int, input().split()))
        for _ in range(n)
]

x, y = 0, 0

# dx,dy (0: 북, 1: 남, 2: 동, 3: 서)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

for x in range(n):
    for y in range(n):
        #(x, y) 기준으로 상하좌우 4칸의 1의 개수를 세어보자.
        cnt = 0 # 상하좌우 4칸의 1의 개수
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]   # 4칸 중 1칸 설정

            if in_range(nx, ny, n) and arr[nx][ny] == 1:   # 인덱스 범위 내에 있고 그 요소가 1이라면 카운트
                cnt +=1


        if cnt >= 3:    # 해당 요소의 상하좌웃 1의 개수가 3개라면 answer 1증가
            answer += 1

# 출력
print(answer)