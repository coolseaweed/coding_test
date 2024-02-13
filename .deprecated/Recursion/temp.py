import sys
input = sys.stdin.readline


#############
## 시간초과 ##
#############

# def solution(N):
#     if N == 1: 
#         table['1'] +=1
#         return

#     for c in str(N):
#         table[c] +=1
#     solution(N-1)



def solution(N, point):

    # 1의 자리수 9로 만들기
    while N % 10 != 9:
        for c in str(N): 
            table[int(c)] += point
        N -= 1

    # 10의 자리수 만큼 더해주기
    for i in range(10): 
        table[i] += (N//10 + 1)*point
    table[0] -= point

    if N < 10: return

    solution(N//10, point*10)


N = int(input().strip())

table = {}
for i in range(10):
    table[i] = 0


solution(N,1)
answer = ''
for i in range(10):
    answer += str(table[i]) + ' '

print(answer)

