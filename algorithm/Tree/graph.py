

# graph = { "a" : ["b","c"],
#           "b" : ["a", "d"],
#           "c" : ["a", "d"],
#           "d" : ["e"],
#           "e" : ["d",'f'],
#           'f' : ['g', 'h'],
#           'h' : ['g']
#          }


graph = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ['b','c','e', 'f'],
          "e" : ["d",'g'],
          'f' : ['g']
         }



def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            if n in graph:
                # temp.sort(reverse=True)
                stack += list(set(graph[n]) - set(visited))
        
    print(visited)

    return visited

def bfs(graph, root):
    visited = []
    queue = [root]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            if n in graph:
                queue += list(set(graph[n]) - set(visited))

    print(visited)

    return visited


dfs(graph,'a')
bfs(graph,'a')