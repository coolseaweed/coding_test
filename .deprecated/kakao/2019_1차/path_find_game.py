
from operator import itemgetter, attrgetter

class Node(object):

    def __init__(self, data):
        self.data = data

        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
    

    def insert(self,data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None

    def insert_value(self,node,data):
        if node is None:
            node = Node(data)
        else :
            if data[0] <= node.data[0]:
                node.left = self.insert_value(node.left, data)
            else :
                node.right = self.insert_value(node.right, data)
        
        return node
    

def preOrder(node, order_list):

    if node == None:
        return -1
    
    print('node : %d\t| [x,y] : [%d,%d]' % (node.data[2],node.data[0],node.data[1]))
    order_list.append(node.data[2])
    preOrder(node.left,order_list)
    preOrder(node.right,order_list)


def postOrder(node, order_list):

    if node == None:
        return -1

    postOrder(node.left,order_list)
    postOrder(node.right,order_list)
    print('node : %d\t| [x,y] : [%d,%d]' % (node.data[2],node.data[0],node.data[1]))
    order_list.append(node.data[2])



def inOrder(node, order_list):

    if node == None:
        return -1

    inOrder(node.left,order_list)
    print('node : %d\t| [x,y] : [%d,%d]' % (node.data[2],node.data[0],node.data[1]))
    order_list.append(node.data[2])
    inOrder(node.right,order_list)



def solution(nodeinfo):

    answer = []

    for index, data in enumerate(nodeinfo):
        data.append(index+1)
    nodeinfo = sorted(nodeinfo, key=itemgetter(1), reverse=True)
    
    BST = BinarySearchTree()
    for item in nodeinfo:
        BST.insert(item)
    
    temp = []
    preOrder(BST.root, temp)    
    answer.append(temp)
    
    temp = []
    postOrder(BST.root, temp)
    answer.append(temp)

    #inOrder(BST.root, temp)
    return answer



nodeInfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
answer = solution(nodeInfo)

print(answer)