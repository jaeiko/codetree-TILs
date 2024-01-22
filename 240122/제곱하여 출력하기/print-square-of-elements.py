_ = int(input())
arr = list(map(int, input().split()))

square_arr = [elem * elem for elem in arr]  # list comprehension : 리스트로 씌어주면 리스트에 요소가 채워진채로 출력

# 만약 그냥 리스트 안쓰고 elem for elem in square_arr 라고 쓰면 generator 를 생성하는 표현식이 된다.
# generator 를 생성하면 generator 객체를 반환한다.. 함수 자체를 print 한 것과 마찬가지.
# ex) print(elem * elem for elem in arr) => <generator object <genexpr> at 0x00001522b7414ce0>

for elem in square_arr:
    print(elem, end = ' ')