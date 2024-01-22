_ = int(input())    #사용하지 않는 변수의 이름은 _로 명명

arr = list(map(int, input().split()))

for elem in arr[::-1]:
    if elem % 2 == 0:
        print(elem, end = ' ')