
import sys

input = sys.stdin.readline


def binarySearch(target):
    start , end = 0, max(trees)

    while start <= end:

        mid = (start+end)//2

        SUM = 0

        for tree in trees:
            if tree > mid:
                SUM += tree - mid


        if SUM < target:
            end = mid -1

        elif SUM >= target:
            answer = mid
            start = mid + 1

    return answer


N, M = map(int,input().split())
trees = list(map(int,input().split()))



print(binarySearch(M))
