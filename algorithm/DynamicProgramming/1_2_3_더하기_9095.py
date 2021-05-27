
import sys

input = sys.stdin.readline

##########
## 설명 ##
##########

# A(n) = A(n-1)+A(n-2)+A(n-3)
# 예를 들어 5의 경우
# 1 +가 되었을 때 5의 경우 = 1 + (모든 4의 경우): A(n-1)    
# 2 +가 되었을 때 5의 경우 = 2 + (모든 3의 경우): A(n-2)
# 3 +가 되었을 때 5의 경우 = 3 + (모든 2의 경우): A(n-3)



N = int(input().strip())

test_case = [int(input().strip()) for _ in range(N)]


integer_list = [1, 2, 4]

for i in range(4, 11):
    integer_list.append(integer_list[-1] + integer_list[-2] + integer_list[-3])


for test in test_case:
    answer = integer_list[test-1]
    print(answer)