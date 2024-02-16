# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root: TreeNode):

    q = [root] if root else []

    while q:

        row = []

        for _ in range(len(q)):
            node = q.pop(0)

            if node:
                row.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                row.append("null")
        # check is symetric
        if row != row[::-1]:
            return False

    return True


if __name__ == "__main__":

    root = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            right=TreeNode(val=3),
        ),
        right=TreeNode(
            val=2,
            left=TreeNode(val=3),
        ),
    )

    answer = bfs(root)

    print(f"ANSWER: {answer}")
