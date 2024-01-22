n = int(input())
score_arr = list(map(float, input().split()))

print(f'{sum(score_arr) / n:.1f}')
if(sum(score_arr) / n >= 4.0):
    print('Perfect')
elif(sum(score_arr) / n >= 3.0):
    print('Good')
else:
    print('Poor')