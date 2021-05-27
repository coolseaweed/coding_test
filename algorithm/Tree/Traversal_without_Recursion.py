


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
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


    def InOderTraversal(self, root):

        stack = []      
        res = []
        curr = root
        while True:
            
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                res.append(curr.data)
                curr = curr.right
            else: break
        return res

    def PreOrderTraversal(self, root):

        stack = [root]      
        res = []
        while len(stack) != 0:

            curr = stack.pop()
            res.append(curr.data)
            n = curr.right
            if n != None: stack.append(n)
            n = curr.left
            if n != None: stack.append(n)

        return res

    def PostOrderTraversal(self, root):


        stack1 = [root]      
        stack2 = []      
        res = []

        while stack1:
            curr = stack1.pop()
            stack2.append(curr)

            if curr.left: stack1.append(curr.left)
            if curr.right: stack1.append(curr.right)
        
        while stack2:
            curr = stack2.pop()
            res.append(curr.data)


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
print(root.InOderTraversal(root))
print(root.PreOrderTraversal(root))
print(root.PostOrderTraversal(root))
