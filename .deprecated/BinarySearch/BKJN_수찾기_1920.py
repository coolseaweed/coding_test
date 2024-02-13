
import sys

input = sys.stdin.readline


def find(data, target, start, end): 
    mid = (start + end) // 2 


    if start >= end: return False 
    if data[mid] == target: return True 
    elif data[mid] > target: return find(data,target, start, mid) 
    else: return find(data,target,mid+1, end)


N = int(input().strip())
num_list = list(map(int,input().strip().split(' ')))

M = int(input().strip())
search_nums = list(map(int,input().strip().split(' ')))


num_list = sorted(num_list)

for target_num in search_nums:

    print(1 if find(num_list,target_num,0, N) else 0)

