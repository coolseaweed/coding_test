import sys
from collections import deque
input = sys.stdin.readline


###################
# memory overflow #
###################

# def solution(RGB_cost):


#     R,G,B = RGB_cost[0]
#     queue = deque([(0,R),(1,G),(2,B)])


#     for RGB in RGB_cost[1:]:
#         R,G,B = RGB
#         next_queue = []

#         while len(queue) != 0:
#             temp = queue.popleft()

#             if temp[0] == 0:
#                 next_queue.append((1,temp[1] + G))
#                 next_queue.append((2,temp[1] + B))
            
#             elif temp[0] == 1:
#                 next_queue.append((0,temp[1] + R))
#                 next_queue.append((2,temp[1] + B))

#             else :
#                 next_queue.append((0,temp[1] + R))
#                 next_queue.append((1,temp[1] + G))

#             # print(next_queue)
#             # input()
        
#         queue = deque(next_queue)

#     return min(queue)[1]



def solution(RGB_cost):

    dp = []
    for i in range(len(RGB_cost)):
        if i == 0:
            dp.append(RGB_cost[i])
            continue

        # R G B cost cal
        R = RGB_cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        G = RGB_cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        B = RGB_cost[i][2] + min(dp[i-1][0], dp[i-1][1])

        dp.append([R,G,B])

    return min(dp[-1])

n = int(input().strip())

test_case = [list(map(int,input().strip().split(' '))) for _ in range(n)]


answer = solution(test_case)
print(answer)
