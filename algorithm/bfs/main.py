from collections import deque


def BFS(graph, root):

    queue, visited = deque([root]), []

    # 현재 노드를 방문 처리
    visited.append(root)

    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        node = queue.popleft()
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

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

    path = BFS(graph, "A")
    print(path)
