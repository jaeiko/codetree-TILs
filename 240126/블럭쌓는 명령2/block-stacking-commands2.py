n, k = tuple(map(int, input().split())) # 총 n개의 칸, k번 반복

block = [0] * n # n개의 블럭칸 생성


for i in range(k):
    a, b = tuple(map(int, input().split()))     # 구간 입력 (a~b)
    for j in range(a-1, b): # a-1 ~  b-1까지 블럭 1 증가(리스트 인덱스는 0부터 시작한다는 점을 감안)
        block[j] += 1

# 최댓값 출력
print(max(block))