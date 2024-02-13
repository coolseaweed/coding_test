
import sys

input = sys.stdin.readline




N = int(input().strip())

ropes = []
for _ in range(N):
    ropes.append(int(input().strip()))


# ropes = [10, 20, 30 , 40 , 50]

ropes = sorted(ropes, reverse=True)

max_weight = 0

for i, rope in enumerate(ropes):
    temp = rope * (i+1)
    max_weight = max(max_weight,temp)
    

print(max_weight)