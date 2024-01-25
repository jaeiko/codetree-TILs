# 단어1, 2 입력
word1 = input()
word2 = input()

# 단어1, 2를 리스트로 변환 후 정렬(str은 바로 sort() 함수를 못쓰므로)
word1_list = sorted(list(word1))
word2_list = sorted(list(word2))

# 다시 분리한 알파벳들을 join으로 연결시켜 단어로 만들고 비교
if ''.join(word1_list) == ''.join(word2_list):
    print('Yes')
else:
    print('No')