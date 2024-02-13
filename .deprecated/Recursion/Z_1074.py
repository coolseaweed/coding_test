import sys
input = sys.stdin.readline


###############
## 시간 초과 ##
##############

# def search(size, row, col):

#     global cnt
#     if size <= 2:
#         if row == r and col == c: return True

#         cnt += 1
#         if row == r and col+1 == c: return True

#         cnt += 1        
#         if row+1 == r and col == c: return True

#         cnt += 1        
#         if row+1 == r and col+1 == c: return True

#         cnt += 1        
#         return False
    
#     check = search(size//2, row, col)
#     if check : return True

#     check = search(size//2, row, col + size//2)
#     if check : return True

#     check = search(size//2, row + size//2, col)
#     if check : return True

#     check = search(size//2, row + size//2, col + size//2)
#     if check : return True



def search(size, r, c, start):
    if size == 1: 
        print(start)
        return 0 

    # 1 사분면
    if  r < size//2 and  c < size//2: 
        #print(f'check 1 {start}')
        search(size//2, r, c, start)

    # 2 사분면
    elif r < size//2 and c >= size//2: 
        #print(f'check 2 {start}')
        search(size//2, r, c - size//2, start + (size//2)**2)

    # 3 사분면
    elif r >= size//2 and c < size//2: 
        #print(f'check 3 {start}')
        search(size//2, r - size//2, c, start + (size//2)**2*2)

    # 4 사분면
    if r >= size//2 and c >= size//2: 
        #print(f'check 4 {start}')
        search(size//2, r - size//2, c - size//2, start + (size//2)**2*3)




N, r, c = map(int,input().strip().split(' '))

search(2**N, r, c, 0)

# test_case = [
#     (2, 0, 0, 0),
#     (2, 0, 1, 1),
#     (2, 0, 2, 4),
#     (2, 0, 3, 5),

#     (2, 1, 0, 2),
#     (2, 1, 1, 3),    
#     (2, 1, 2, 6),    
#     (2, 1, 3, 7),   

#     (2, 2, 0, 8),
#     (2, 2, 1, 9),
#     (2, 2, 2, 12),
#     (2, 2, 3, 13),

#     (2, 3, 0, 10),
#     (2, 3, 1, 11),    
#     (2, 3, 2, 14),    
#     (2, 3, 3, 15),   

# ]


# for case in test_case:
#     N, r, c , answer  = case
#     print(answer)
#     search(2**N, r, c, 0)
#     print('-------------------')












#print(cnt)