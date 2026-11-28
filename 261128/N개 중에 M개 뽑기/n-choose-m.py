answer = []

def print_answer():
    for num in answer:
        print(f"{num}", end =' ')

    print()

def choose(curr_num, n, m, last_num):
    if (curr_num == m+1):
        print_answer()
        return

    for select in range(last_num + 1, n+1):
        answer.append(select)
        choose(curr_num + 1, n, m, select)
        answer.pop()


# N개의 정수 중 M개를 고르기
N, M = map(int, input().split())

# Please write your code here.
choose(1, N, M, 0)
