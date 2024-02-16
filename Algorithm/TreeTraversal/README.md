# Tree Traversal

<p align="center">
<img src = "https://upload.wikimedia.org/wikipedia/commons/a/ac/Preorder-traversal.gif" width="250">
<img src = "https://upload.wikimedia.org/wikipedia/commons/4/48/Inorder-traversal.gif" width="250">
<img src = "https://upload.wikimedia.org/wikipedia/commons/2/28/Postorder-traversal.gif" width="250">
</p>

Tree 의 모든 노드들을 방문하는 과정을 트리 순회(TreeTraversal)라고 한다.

## Pseudocode
### Pre-Order (DFS)
- **Recursive Implementation**
    ```bash
    procedure preorder(node)
    if node = null
        return
    visit(node)
    preorder(node.left)
    preorder(node.right)
    ```
- **Iterative Implementation**
    ```bash
    procedure iterativePreorder(node)
    if node = null
        return
    stack ← empty stack
    stack.push(node)
    while not stack.isEmpty()
        node ← stack.pop()
        visit(node)
        // right child is pushed first so that left is processed first
        if node.right ≠ null
            stack.push(node.right)
        if node.left ≠ null
            stack.push(node.left)
    ```
    [Go to python code](./preorder.py)

### In-Order 
- **Recursive Implementation**
    ```bash
    procedure preorder(node)
    if node = null
        return
    preorder(node.left)
    visit(node)
    preorder(node.right)
    ```
- **Iterative Implementation**
    ```bash
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
    ```
    [Go to python code](./inorder.py)


### Post-Order
- **Recursive Implementation**
    ```bash
    procedure preorder(node)
    if node = null
        return
    preorder(node.left)
    preorder(node.right)
    visit(node)
    ```

- **Iterative Implementation**
    ```bash
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
    ```
    [Go to python code](./postorder.py)




