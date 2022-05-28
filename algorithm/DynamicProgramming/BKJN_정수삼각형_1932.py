import sys
input = sys.stdin.readline


def solution(steps, n):

    dp = []
    dp.append(steps[0])
    if n == 1: return max(dp[-1])
    dp.append([steps[0][0]+steps[1][0],steps[0][0]+steps[1][1]])
    if n == 2: return max(dp[-1])

    for i in range(2,n):
        
        cur = steps[i]
        prev = dp[i-1]

        temp_list = []
        for j in range(len(cur)):
            if j == 0: 
                temp_list.append(prev[0]+ cur[0])
                continue
            elif j == len(cur)-1: 
                temp_list.append(prev[-1]+ cur[j])
                continue
            temp_list.append(max(prev[j-1]+ cur[j],prev[j]+ cur[j]))
        dp.append(temp_list)

    return max(dp[-1])


n = int(input().strip())

steps = [list(map(int,input().strip().split(' '))) for _ in range(n)]

answer = solution(steps,n)
print(answer)
