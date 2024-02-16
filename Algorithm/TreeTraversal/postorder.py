from collections import deque
from Tree import Node


def iterativePostorder(node):

    stack, visited, last_visted_node = deque([]), [], None
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visted_node != peek_node.right:
                node = peek_node.right
            else:
                visited.append(peek_node.val)
                last_visted_node = stack.pop()
    return visited


def recursivePostorder(root):
    visited = []
    if root:
        visited += recursivePostorder(root.left)
        visited += recursivePostorder(root.right)
        visited.append(root.val)

    return visited


if __name__ == "__main__":

    # insert item into Node
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

    iter_path = iterativePostorder(root)
    recur_path = recursivePostorder(root)

    print(f"iterative: {iter_path} \nrecursive: {recur_path}")
