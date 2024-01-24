# Boom 클래스
class BombInfo:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

# 해제 코드, 끊어야하는 선의 색, 특정 초 입력
code, color, second = list(map(str, input().split()))
bomb1 = BombInfo(code, color, second)   # 객체에 저장

# 출력
print(f'code : {bomb1.code}')
print(f'color : {bomb1.color}')
print(f'second : {bomb1.second}')