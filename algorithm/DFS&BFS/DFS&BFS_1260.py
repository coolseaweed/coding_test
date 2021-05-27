from collections import deque
from sys import stdin



def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp

    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp

    return " ".join(str(i) for i in visited)

  

graph = {}

node, edge, start = map(int,stdin.readline().split(' '))


# 그래프 생성
for i in range(node): 
    graph[i+1] = []

for _ in range(edge):
    u, v = map(int, stdin.readline().split(" "))
    graph[u].append(v)
    graph[v].append(u)


# 탐색
print(DFS(graph, start))
print(BFS(graph, start))
