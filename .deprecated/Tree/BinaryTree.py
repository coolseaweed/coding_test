


class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    # Insert Nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    # print the Tree
    def show(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


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


    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res += self.inorder_traversal(root.right)
        return res

    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorder_traversal(root.left)
            res += self.preorder_traversal(root.right)

        return res

    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res += self.postorder_traversal(root.right)
            res.append(root.data)
        return res

# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# print(root.PreoerderTraversal(root))


root = Node(100)
root.insert(50)
root.insert(150)
root.insert(25)
root.insert(75)
root.insert(125)
root.insert(175)
root.insert(110)
print(root.inorder_traversal(root))
print(root.preorder_traversal(root))
print(root.postorder_traversal(root))
root.search(99)