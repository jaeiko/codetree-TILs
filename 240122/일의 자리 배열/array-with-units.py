pp, p = map(int, input().split())    # pp : 전전항 / p : 전항

print(pp, p, end=' ')
for _ in range(8):
    pp, p = p, pp + p
    print(p % 10, end=' ')