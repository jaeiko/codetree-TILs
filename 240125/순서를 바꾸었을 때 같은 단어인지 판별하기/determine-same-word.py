word1 = input()
word2 = input()

word1_list = sorted(list(word1))
word2_list = sorted(list(word2))

if ''.join(word1_list) == ''.join(word2_list):
    print('Yes')
else:
    print('No')