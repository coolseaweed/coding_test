from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def BFS(root: TreeNode):

    q, answer = deque([root] if root else []), []

    while q:

        row = []

        for _ in range(len(q)):
            node = q.popleft()

            if node:
                row.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                row.append(None)

        answer.append(row)
    return answer


if __name__ == "__main__":

    # insert item into Node
    root = TreeNode(
        val=3,
        left=TreeNode(
            val=9,
        ),
        right=TreeNode(
            val=20,
            left=TreeNode(val=15),
            right=TreeNode(val=7),
        ),
    )

    answer = BFS(root)

    print(f"ANSWER: {answer}")
