import sys

# Info 클래스
class Info:
    def __init__(self, code_name, score):
        self.code_name = code_name  # 코드네임
        self.score = score          # 점수\
 
# 객체 저장할 리스트
info_list = []
#최소 점수를 가지는 이름과 점수 변수
min_score_name = ''
min_score = sys.maxsize

# 반복문을 통해 code_name과 score을 입력받아 객체 생성 -> 리스트에 추가
# 값을 비교하여 더 점수가 작으면 해당 점수와 이름으로 min_score_name, min_score 갱신
for i in range(5):
    code_name, score = list(map(str, input().split()))
    info_list.append(Info(code_name, int(score)))
    if min_score > info_list[i].score:
        min_score_name = info_list[i].code_name
        min_score = info_list[i].score

print(min_score_name, min_score)