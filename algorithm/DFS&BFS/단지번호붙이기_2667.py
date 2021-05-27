from sys import stdin
read = lambda : stdin.readline().strip()


def bfs(matrix, cnt, x, y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 그래서 0으로 바꾼다
    queue = []
    queue.append((x, y))

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while len(queue) > 0:
        x, y = queue.pop(0)
        for k in range(0, 4):
            nx, ny = x + dx[k], y + dy[k]
            if nx <0  or nx> n-1 or ny<0 or ny >n-1: continue
            if matrix[nx][ny] == 1:
                cnt += 1
                matrix[nx][ny] = 0
                queue.append((nx, ny))

    return cnt


def dfs(matrix, cnt, x,y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 하고 0으로 바꾸는것 이다.
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]


    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]
        # 이 근처 다 n_x, n_y로 간다.
        if n_x>=0 and n_x<n and n_y>=0 and n_y<n:
            # 범위 check
            if matrix[n_x][n_y]==1:
            # 그부분이 1이면
                cnt = dfs(matrix, cnt+1, n_x, n_y)
                # cnt를 증가시켜서 다시한번 그 근처 확인

    return cnt
    # 다 cnt검사하면 끝을 낸다.




n = int(read())

matrix = [list(map(int, list(read()))) for _ in range(n)]



# n = 7
# matrix=[
#     [0,1,1,0,1,0,0],
#     [0,1,1,0,1,0,1],
#     [1,1,1,0,1,0,1],
#     [0,0,0,0,1,1,1],
#     [0,1,0,0,0,0,0],
#     [0,1,1,1,1,1,0],
#     [0,1,1,1,0,0,0]
# ]

ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            #ans.append(bfs(matrix, 1, i, j))
            ans.append(dfs(matrix, 1, i, j))
            # 여기서 이제 그 주위에 있는 것들 다 돌아보는것이다.
print(len(ans))
for i in sorted(ans):
    print(i)



