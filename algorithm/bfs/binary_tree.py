from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root: TreeNode) -> List[List[int]]:

    q, answer = deque([root] if root else []), []

    while q:

        row = []

        for _ in range(len(q)):
            node = q.popleft()
            row.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        answer.append(row)
    return answer


if __name__ == "__main__":

    # insert item into Node
    root = TreeNode(
        val=3,
        left=TreeNode(
            val=9,
            left=TreeNode(val=None),
            right=TreeNode(val=None),
        ),
        right=TreeNode(
            val=20,
            left=TreeNode(val=15),
            right=TreeNode(val=7),
        ),
    )

    answer = bfs(root)

    print(f"ANSWER: {answer}")
