
import sys

input = sys.stdin.readline




N = int(input().strip())
times = []
for _ in range(N):
    start, end = map(int, input().strip().split(' '))
    gap = end - start

    times.append((start,end,gap))

times = sorted(times, key =(lambda x:x[2]))
print(times)