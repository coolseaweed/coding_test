
import sys

input = sys.stdin.readline


def factorial(n):
    if n == 1 : return 1

    return n * factorial(n-1)

def combination(n,r):
    if n == r : return 1
    else: return factorial(n)//(factorial(r)*factorial(n-r))


n, r = map(int,input().strip().split(' '))



answer = combination(n,r)
print(answer)