
from itertools import combinations
from copy import deepcopy


max_safe_area = 0

def spread_virus(arr, walls, virus_list, N, M, safe_area):

    visited=[]
    tmp_arr = deepcopy(arr)
    global max_safe_area



    for wall in walls:
        y,x = wall
        tmp_arr[y][x] = 1


    queue = deepcopy(virus_list)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]


    while len(queue) != 0:
        y, x = queue.pop(0)
        for i in range(4):
            loc_y = y + dy[i]
            loc_x = x + dx[i]

            if 0 > loc_x or loc_x >= M or 0 > loc_y or loc_y >= N:  continue
            if tmp_arr[loc_y][loc_x] : continue

            tmp_arr[loc_y][loc_x] = 2
            queue.append([loc_y,loc_x])
            safe_area -= 1

            if safe_area <= max_safe_area !=0 : return 0


    max_safe_area = safe_area



N, M = map(int, input().split(' '))
arr = []
arr = [list(map(int, input().split())) for _ in range(N)]


# N,M=(7,7)
# arr=[
#     [2, 0, 0, 0, 1, 1, 0],
#     [0, 0, 1, 0, 1, 2, 0],
#     [0, 1, 1, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 1],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0]
# ]


# N,M=(4,6)
# arr=[
#     [0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 2],
#     [1, 1, 1, 0, 0, 2],
#     [0, 0, 0, 0, 0, 2]
# ]

virus_list = []
area_list = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:  virus_list.append([i,j])
        elif arr[i][j] == 0:  area_list.append([i,j])


safe_area = len(area_list)

for walls in combinations(area_list,3):
    spread_virus(arr, walls, virus_list, N,M, safe_area-3)

print(max_safe_area)

