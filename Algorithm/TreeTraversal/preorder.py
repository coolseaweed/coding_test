from collections import deque
from Tree import Node


def iterativePreorder(root):

    stack, visited = deque([root] if root else []), []
    while stack:
        node = stack.pop()
        visited.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def recursivePreorder(root):
    visited = []
    if root:
        visited.append(root.val)
        visited += recursivePreorder(root.left)
        visited += recursivePreorder(root.right)

    return visited


if __name__ == "__main__":

    # create graphs
    root = Node(
        val="F",
        left=Node(
            val="B",
            left=Node(val="A"),
            right=Node(
                val="D",
                left=Node("C"),
                right=Node("E"),
            ),
        ),
        right=Node(
            val="G",
            right=Node(
                val="I",
                left=Node("H"),
            ),
        ),
    )

    iter_path = iterativePreorder(root)
    recur_path = recursivePreorder(root)

    print(f"iterative: {iter_path} \nrecursive: {recur_path}")
