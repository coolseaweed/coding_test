# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrder(root):
    visited = []
    if root:
        visited.append(root.val)
        visited += preOrder(root.left)
        visited += preOrder(root.right)

    return visited


def inOrder(root):
    visited = []
    if root:
        visited += inOrder(root.left)
        visited.append(root.val)
        visited += inOrder(root.right)

    return visited


def postOrder(root):
    visited = []
    if root:
        visited += postOrder(root.left)
        visited += postOrder(root.right)
        visited.append(root.val)

    return visited


if __name__ == "__main__":

    # insert item into Node
    root = TreeNode(
        val="F",
        left=TreeNode(
            val="B",
            left=TreeNode(val="A"),
            right=TreeNode(
                val="D",
                left=TreeNode("C"),
                right=TreeNode("E"),
            ),
        ),
        right=TreeNode(
            val="G",
            right=TreeNode(
                val="I",
                left=TreeNode("H"),
            ),
        ),
    )

    # Inorder traversal
    preorder_path = preOrder(root)
    inorder_path = inOrder(root)
    postorder_path = postOrder(root)

    print(f"Pre-Order path: {preorder_path}\nIn-Order path: {inorder_path}\nPost-Order path: {postorder_path}\n")
