
import sys
from itertools import permutations


input = sys.stdin.readline


N = list(map(str, input().strip()))

temp = ''
for i in sorted(N, reverse =True):
    temp += i

temp = int(temp)
if temp %30 == 0:
    print(temp)
else:
    print(-1)

