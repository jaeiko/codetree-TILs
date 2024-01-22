pp, p = map(int, input().split())

print(pp, p, end=' ')
for i in range(8):
    pp, p = p, (2 * pp) + p
    print(p, end=' ')