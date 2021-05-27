

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def show_preorder(self):
        print(self.data)
        if self.left:
            self.left.show_preorder()
        if self.right:
            self.right.show_preorder()

    
    def show_inorder(self):

        if self.left:
            self.left.show_inorder()
        print(self.data)
        if self.right:
            self.right.show_inorder()

    
    def show_postorder(self):
        if self.left:
            self.left.show_postorder()
        if self.right:
            self.right.show_postorder()
        print(self.data)


    def search(self, key):
        if key < self.data:
            if self.left is None:
                print(f'{key} is not found!')
                return
            return self.left.search(key)
        elif key > self.data:
            if self.right is None:
                print(f'{key} is not found!')
                return 
            return self.right.search(key)

        else:
            print(f'{key} is found!')





def dfs(root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n.data not in visited:
            visited.append(n.data)
        if n.right is not None: 
            stack.append(n.right)
        if n.left is not None: 
            stack.append(n.left)
    print(visited)

    return visited


def bfs(root):
    visited = []
    queue = [root]

    while queue:
        n = queue.pop(0)
        if n.data not in visited:
            visited.append(n.data)
        if n.left is not None: 
            queue.append(n.left)
        if n.right is not None: 
            queue.append(n.right)

    print(visited)

    return visited






root = Node(100)
root.insert(50)
root.insert(150)
root.insert(25)
root.insert(75)
root.insert(125)
root.insert(175)
root.insert(110)
print('------------------------')
root.show_inorder()
print('------------------------')
root.show_preorder()
print('------------------------')
root.show_postorder()
print('------------------------')
dfs(root)
print('------------------------')
bfs(root)

root.search(110)






