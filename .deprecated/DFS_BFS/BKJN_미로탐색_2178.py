

##############     
## method 1 ##      runtime: 4688ms
############## 

def BFS_1(maze, start, target):
    visited = []
    N,M = target
    queue = [start]

    distance = [[0 for _ in range(M)] for _ in range(N)]
    distance[0][0] = 1 


    while queue:
        [y,x] = queue.pop(0)
        visited.append([y,x])

        # 상하좌우 순서로 탐색
        if y > 0 and maze[y-1][x] == 1 and [y-1,x] not in visited and [y-1,x] not in queue:
            queue.append([y-1,x])
            distance[y-1][x] = distance[y][x] +1

        if y < N-1 and maze[y+1][x] == 1 and [y+1,x] not in visited and [y+1,x] not in queue:
            queue.append([y+1,x])
            distance[y+1][x] = distance[y][x] +1

        if x > 0 and maze[y][x-1] == 1 and [y,x-1] not in visited and [y,x-1] not in queue:
            queue.append([y,x-1])
            distance[y][x-1] = distance[y][x] +1

        if x < M-1 and maze[y][x+1] == 1 and [y,x+1] not in visited and [y,x+1] not in queue:
            queue.append([y,x+1])
            distance[y][x+1] = distance[y][x] +1

    return distance[N-1][M-1]




##############      
## method 2 ##      runtime: 180 ms
############## 


def BFS_2(maze, start, target):
    n, m = target
    
    queue = [start]
   
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    while len(queue) != 0:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if 0 > nx or nx >= n: continue
            if 0 > ny or ny >= m: continue
            if maze[nx][ny] == 0: continue
            if visited[nx][ny] != 0: continue
    
            visited[nx][ny] = visited[x][y] + 1
            queue.append([nx,ny])
    
    return visited[n-1][m-1]



N, M = map(int, input().split(' '))
maze = []
for _ in range(N):
    maze.append(list(map(int,str(input()))))

temp1 = BFS_1(maze,[0,0], [N,M])
temp2 = BFS_2(maze,[0,0], [N,M])

print(temp1,temp2)


