n, k, t = list(map(str, input().split()))

word_list = []

for _ in range(int(n)):
    word = input()
    if t in word[0:len(t)]:
        word_list.append(word)

sort(word_list)

print(word_list[int(k)])