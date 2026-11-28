answer = []

def print_answer():
    for num in answer:
        print(f"{num} ", end='')
    print()

def choose(curr_num, n, k):
    if(curr_num == n):
        print_answer()
        return

    for select in range(1, k+1):
        answer.append(select)
        choose(curr_num + 1, n, k)
        answer.pop()
    


K, N = map(int, input().split())

# Please write your code here.

choose(0, N, K);
