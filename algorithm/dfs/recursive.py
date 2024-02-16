from collections import deque


def DFS_recursive(graph, root, visited=[]):

    visited.append(root)
    for node in graph[root]:
        if node not in visited:
            DFS_recursive(graph, node, visited)

    return visited


if __name__ == "__main__":

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "G", "H", "I"],
        "D": ["B", "E", "F"],
        "E": ["D"],
        "F": ["D"],
        "G": ["C"],
        "H": ["C"],
        "I": ["C", "J"],
        "J": ["I"],
    }

    path = DFS_recursive(graph, "A")
    print(path)
