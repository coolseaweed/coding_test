import sys
input = sys.stdin.readline


def cal(n):
    temp = 1
    for i in range(1,n):
        temp += 2**i
    return temp



def move(n, src, auxil, dest):
    if n == 1:
        print(f'{src} {dest}')
        return 

    move(n-1, src, dest, auxil)
    print(f'{src} {dest}')
    move(n-1, auxil, src, dest)

N = int(input().strip())

num = cal(N)

print(num)
if N <= 20: move(N, 1, 2, 3 )
