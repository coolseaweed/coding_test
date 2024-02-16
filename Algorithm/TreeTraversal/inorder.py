from collections import deque
from Tree import Node

"""
procedure iterativePostorder(node)
    stack ← empty stack
    lastNodeVisited ← null
    while not stack.isEmpty() or node ≠ null
        if node ≠ null
            stack.push(node)
            node ← node.left
        else
            peekNode ← stack.peek()
            // if right child exists and traversing node
            // from left child, then move right
            if peekNode.right ≠ null and lastNodeVisited ≠ peekNode.right
                node ← peekNode.right
            else
                visit(peekNode)
                lastNodeVisited ← stack.pop()
"""


def iterativeInorder(node):

    stack, visited = deque([]), []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            visited.append(node.val)
            node = node.right

    return visited


def recursiveInorder(root):
    visited = []
    if root:
        visited += recursiveInorder(root.left)
        visited.append(root.val)
        visited += recursiveInorder(root.right)

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

    iter_path = iterativeInorder(root)
    recur_path = recursiveInorder(root)

    print(f"iterative: {iter_path} \nrecursive: {recur_path}")
