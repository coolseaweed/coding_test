import sys

input = sys.stdin.readline




def solution(n):
    
    result = [0]*(n+1)

    result[0] = result[1] = 1

    for i in range(2,n+1):
        result[i] = (result[i-1]+result[i-2])%10007


    return result[n]




n = int(input().strip())


answer = solution(n)
print(answer)


