
import sys


input = sys.stdin.readline


def cal(case):
    results = []

    for n in case:
        results.append(n-1)        

        if n % 3 == 0:
            results.append(n//3)
        
        if n % 2 == 0:
            results.append(n//2)
    
    results = list(set(results))
    return results




def solution(n):
    cnt = 0
    if n == 1:
        return cnt

    results = [n]
    while True:

        temp = results
        results = []
        results = cal(temp)

        cnt += 1

        if min(results) == 1:
            break

    return cnt
N = int(input().strip())



answer = solution(N)
print(answer)