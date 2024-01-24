#1. 입력
n = int(input())    # 단어의 개수 n
words = [input() for _ in range(n)]

#2. 정렬하기
words.sort()

for word in words:
    print(word)