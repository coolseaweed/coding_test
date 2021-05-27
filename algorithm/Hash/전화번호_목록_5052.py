
import sys

input = sys.stdin.readline


def solution(phone_book): 
    phone_book.sort() 
    for i in range(len(phone_book)-1): 
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]: 
            return 'NO'
    return 'YES'


N = int(input().strip())

test_case = []
for _ in range(N):

    i = int(input().strip())
    temp = []
    for _ in range(i):
        temp.append(input().strip())
    test_case.append(temp)

for test in test_case:
    answer = solution(test)
    print(answer)

