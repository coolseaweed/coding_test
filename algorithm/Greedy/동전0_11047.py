
import sys

input = sys.stdin.readline


N, target = map(int, input().split(' '))


coins=[]

for _ in range(N):
    temp = int(input().strip())
    if temp < target:
        coins.append(temp)
coins = sorted(coins, reverse=True)

cnt = 0

for coin in coins:
    cnt += target//coin

    
    if target == 0:
        break

print(cnt)
