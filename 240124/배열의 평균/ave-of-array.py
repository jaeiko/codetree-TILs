arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

total_sum = 0

for i in range(2):
    row_sum_val = 0
    for j in range(4):
        row_sum_val += arr[i][j]
    print(row_sum_val / 4, end=' ')

print()

for i in range(4):
    column_sum_val = 0
    for j in range(2):
        column_sum_val += arr[j][i]
        total_sum += arr[j][i]
    print(column_sum_val / 2, end=' ')

print()
print(f'{total_sum / 8}.1f')