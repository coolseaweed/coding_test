
import sys
input = sys.stdin.readline


def count_fibonacci(n):

    zero_counter = [1,0]
    one_counter = [0,1]

    if n < 2: 
        return zero_counter,one_counter

    for i in range(2, n+1):
        zero_counter.append(zero_counter[i-1]+zero_counter[i-2])
        one_counter.append(one_counter[i-1]+one_counter[i-2])

    return zero_counter,one_counter

N = int(input().strip())
test_case = [int(input().strip()) for _ in range(N)]

for n in test_case:
    zero_counter, one_counter = count_fibonacci(n)

    print(zero_counter[n],one_counter[n])

