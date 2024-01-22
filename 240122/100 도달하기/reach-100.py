p = int(input())
pp = 1
print(pp, p, end=' ')
while True:
    print(pp + p, end=' ')
    pp, p = p, pp + p
    if pp + p >= 100:
        print(pp + p, end=' ')
        break