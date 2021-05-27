
import sys

input = sys.stdin.readline




price = int(input().strip())

# print(price)

coins = [500,100,50,10,5,1]

changes = 1000 - price
cnt = 0
for coin in coins:
    cnt += changes//coin
    changes = changes%coin

print(cnt)