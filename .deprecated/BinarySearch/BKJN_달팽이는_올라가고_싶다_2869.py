
import sys

input = sys.stdin.readline


def find(data, target, start, end): 
    mid = (start + end) // 2 


    if start >= end: return False 
    if data[mid] == target: return True 
    elif data[mid] > target: return find(data,target, start, mid) 
    else: return find(data,target,mid+1, end)


A, B, V = map(int,input().strip().split(' '))
k = (V-B)/(A-B)
print(int(k) if k == int(k) else int(k)+1)	#삼항연산자