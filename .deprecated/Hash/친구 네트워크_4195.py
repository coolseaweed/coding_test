# Hash 
# Find-Union

import sys

input = sys.stdin.readline


def find(x, parent):
    if parent[x] == x: return x
    else:
        p = find(parent[x],parent)
        parent[x] = p
        return p

def union(x,y, parent, number):
    x, y = find(x, parent), find(y, parent)

    if x != y:
        parent[y] = x
        number[x] += number[y]

    print(number[x])


def solution(test_cases):
    
    for test_case in test_cases:

        parent, number = {}, {}
        for network in test_case:

            a, b = network.split(' ')
            if a not in parent:
                parent[a] = a
                number[a] = 1
            if b not in parent:
                parent[b] = b
                number[b] = 1
            union(a,b, parent, number)

N = int(input().strip())

test_cases = []
for _ in range(N):
    num_case = int(input().strip())
    test_case = [input().strip() for _ in range(num_case)]
    test_cases.append(test_case)


solution(test_cases)
