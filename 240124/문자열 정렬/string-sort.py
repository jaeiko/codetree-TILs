# 문자열을 각 문자를 원소로 갖는 list로 변환 후 sort 함수를 이용하면 정렬이 가능
str_word = list(input())
str_word.sort()
sorted_str = ''.join(str_word)  # 다시 join함수를 이용하여 문자열로 변환

print(sorted_str)