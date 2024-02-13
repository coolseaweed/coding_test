
import sys

input = sys.stdin.readline




N = input().strip()

times = list(map(int,input().strip().split(' ')))

times = sorted(times)

take = 0
total = 0
for t in times:
    take += t
    total += take

print(total)