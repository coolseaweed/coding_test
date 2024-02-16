from collections import deque


def DFS(graph, root):

    stack, visited = deque([root]), []

    # 스택이 완전히 빌 때까지 반복
    while stack:
        # 스택에 삽입된 순서대로 노드 하나 꺼내기
        node = stack.pop()

        # 만약 노드가 방문한 목록에 없다면
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

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

    path = DFS(graph, "A")
    print(path)
