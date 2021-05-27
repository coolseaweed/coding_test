import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

#############
## 시간초과 ##
#############

def solution(N):
    if N == 1: 
        table['1'] +=1
        return

    for c in str(N):
        table[c] +=1
    solution(N-1)



# def solution(N):
#     point = 1
#     # 앞자리수 9로 만들기
#     while N % 10 != 9:
#         for c in str(N): 
#             table[int(c)] += point
#         N -= 1

#     # 10씩 나누면서 테이블 채우기
#     while N != 0:
#         if N < 10:
#             for i range(n+1):
#                 table[i] += point
#             table[0] -= point
#         else:
#             for i in range(10):
#                 table[i] += (n//10 + 1) * point
        



N = int(input().strip())

table = {}
for i in range(10):
    table[str(i)] = 0

solution(N)

answer = ''
for i in range(10):
    if i == 9:
        answer += str(table[str(i)])
    else:
        answer += str(table[str(i)]) + ' '

print(answer)





