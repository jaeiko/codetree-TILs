import sys
input = sys.stdin.readline

# 노드 클래스
class Node:
    # 노드의 속성을 제한해 메모리 사용량 감소
    __slots__ = ("data", "prev", "next")

    def __init__(self, data):
        self.data = data    # 저장할 문자열
        self.prev = None    # 이전 노드
        self.next = None    # 다음 노드

# 1번: 현재 노드 앞에 삽입
def insert_prev(u, node):
    # 새 노드의 연결정보 설정
    node.prev = u.prev
    node.next = u

    # 기존 왼쪽 노드의 다음 노드를 변경
    if u.prev is not None:
        u.prev.next = node

    u.prev = node

# 2번: 현재 노드 뒤에 삽입
def insert_next(u, node):
    # 새 노드의 연결 정보 설정
    node.next = u.next
    node.prev = u

    # 기존 오른쪽 노드의 이전 노드를 변경
    if u.next is not None:
        u.next.prev = node
    
    # 현재 노드의 다음 노드를 변경
    u.next = node;

# 이전 / 현재 / 다음 노드 출력
def print_state(u):
    # 이전 노드
    if u.prev is not None:
        prev_data = u.prev.data
    else:
        prev_data = "(Null)"

    # 다음 노드
    if u.next is not None:
        next_data = u.next.data
    else:
        next_data = "(Null)"

    # 현재 노드와 함께 한 줄 출력
    sys.stdout.write(f"{prev_data} {u.data} {next_data}\n")


S_init = input().rstrip("\n")
N = int(input())

command = []
S_value = []

for _ in range(N):
    line = input().split()
    cmd = int(line[0])
    command.append(cmd)

    if cmd == 1 or cmd == 2:
        S_value.append(line[1])
    else:
        S_value.append("")

# Please write your code here.

# 최초 노드 생성
curr = Node(S_init)

# 명령 순서대로 수행
for i in range(N):
    if command[i] == 1 or command[i] == 2:
        # 1, 2번: 삽입할 문자열로 노드 생성
        node = Node(S_value[i])

        if command[i] == 1:
            # 현재 노드 앞에 삽입
            insert_prev(curr, node)
        else:
            # 현재 노드 뒤에 삽입
            insert_next(curr, node)

    elif command[i] == 3:
        # 3번: 이전 노드가 있으면 이동
        if curr.prev is not None:
            curr = curr.prev

    elif command[i] == 4:
        # 4번: 다음 노드가 있으면 이동
        if curr.next is not None:
            curr = curr.next

    # 모든 명령 직후 출력
    print_state(curr)
