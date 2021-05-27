import sys
input = sys.stdin.readline



###########################
# 처음에 생각해 낸 아이디어 #
###########################

# def solution(steps,n):

#     dp = deque()

#     dp.append([(0,1),steps[0],1])
#     dp.append([(0,2),steps[1],2])
#     print(dp)
#     print('\n\n')
#     max_score = 0
#     while len(dp) != 0:


#         history, score, length = dp.popleft()


#         if history[0] == 1 and history[1] == 1:
            
#             if length+2 > n:
#                 continue

#             dp.append([(history[1],2), score + steps[length+2-1], length +2])
#         else:

#             if length+1 > n or length +2 > n:
#                 continue
#             dp.append([(history[1],1), score + steps[length+1-1], length +1])
#             dp.append([(history[1],2), score + steps[length+2-1], length +2])




def solution(steps, n):

    dp = []
    dp.append(steps[0])
    if n == 1: return dp[-1]
    
    dp.append(steps[1]+steps[0])
    if n == 2: return dp[-1]
    
    dp.append(max(steps[0]+steps[2], steps[1]+steps[2]))

    for i in range(3,n):
        dp.append(max(steps[i]+steps[i-1]+dp[i-3], steps[i]+dp[i-2]))

        # print(dp)
    return dp[-1]


n = int(input().strip())

steps = [int(input().strip()) for _ in range(n)]
# print(steps)

answer = solution(steps,n)
print(answer)
