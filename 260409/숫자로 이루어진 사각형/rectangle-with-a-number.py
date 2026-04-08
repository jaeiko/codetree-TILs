n = int(input())
num = 1
# Please write your code here.
def rectangle(n):
    global num

    for i in range(n):
        for j in range(n):
            if num == 10:
                num = 1
            print(num, end=' ')
            num += 1
        print()

rectangle(n)