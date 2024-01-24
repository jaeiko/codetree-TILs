# 상품 클래스
class Goods:
    def __init__(self, name, code):
        self.name = name
        self.code = code


# 상품1 객체 생성
goods1 = Goods("codetree", "50")

# 상품2 정보 입력 후 객체 생성
goods2_name, goods2_code = list(map(str, input().split()))
goods2 = Goods(goods2_name, goods2_code)

# 상품1 정보 출력
print(f'product {goods1.code} is {goods1.name}')
print(f'product {goods2.code} is {goods2.name}')