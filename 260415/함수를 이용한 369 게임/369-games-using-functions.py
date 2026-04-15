a, b = map(int, input().split())

def count_3multiple(a, b):
    count = 0
    for i in range(a, b + 1):
        num_str = str(i)
        # 3의 배수이거나, 숫자에 '3', '6', '9' 중 하나라도 포함된 경우
        # any: 리스트나 문자열 같은 묶음을 훑으면서, 조건에 맞는 게 단 하나라도 있으면 바로 True를 던져줍니다.
        
        # for char in '369': 문자열 '369'에서 '3', '6', '9'를 하나씩 꺼낸다.
        # char in num_str: 꺼낸 글자가 num_str에 들어있는지 확인
        # 결과: 셋 중 하나라도 in(포함)이 성립하면 any는 즉시 True가 된다.
        if i % 3 == 0 or any(char in num_str for char in '369'):
            count += 1
    return count

print(count_3multiple(a, b))
