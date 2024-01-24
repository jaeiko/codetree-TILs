# user_info 클래스
class user_info:
    def __init__(self, user_id, level):
        self.user_id = user_id  # 유저 id
        self.level = level  # 유저 레벨

#user_info 객체 user1, user2 생성
user1 = user_info('codetree', '10')
user2_id, user2_level = list(map(str, input().split()))
user2 = user_info(user2_id, user2_level)

print(f'user {user1.user_id} lv {user1.level}')
print(f'user {user2.user_id} lv {user2.level}')