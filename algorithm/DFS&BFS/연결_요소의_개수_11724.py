
from sys import stdin
from collections import deque



def BFS(graph):

    count = 0
    visited = [0] * (N + 1)

    for i in range(1, len(visited)):
        if visited[i] == 0:
            count += 1
            q = deque([i])    
        while q:
            x = q.popleft()
            for j in graph[x]:
                if visited[j] == 0:
                    q.append(j)
                    visited[j] = 1
    return count

  

N, M = map(int,stdin.readline().split(' '))

graph = {}

for i in range(N): 
    graph[i+1] = []

for _ in range(M):
    u, v = map(int, stdin.readline().split(" "))
    graph[u].append(v)
    graph[v].append(u)


connections = BFS(graph)


print(connections)

# n = 6
# graph = {1: [2, 5], 2: [1, 5], 5: [2, 1], 3: [4], 4: [3, 6], 6: [4]}
# nodes = [i for i in range(1,n+1)]

