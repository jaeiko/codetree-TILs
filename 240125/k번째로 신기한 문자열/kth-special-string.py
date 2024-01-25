# 단어가 n개 주어졌을 때, 문자열 T로 시작하는 단어들 중 사전순으로 정렬했을 때의 k번째 문자열을 출력
n, k, t = list(map(str, input().split()))

word_list = []  # 문자열 T로 시작하는 단어들이 들어갈 리스트

for _ in range(int(n)):
    word = input()          # 단어 입력
    if t in word[0:len(t)]: # 해당 단어가 문자열 T로 시작하는 단어이면 단어 추가
        word_list.append(word)

word_list.sort()    # 리스트 내 단어들을 사전순으로 정렬

print(word_list[int(k)-1])  # 출력(이 때 k는 1부터 이므로 리스트 인덱스 기준에 맞게 -1을 해준다.)