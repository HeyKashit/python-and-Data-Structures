from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Levelorder(root):
    if root is None:
        return
    q=deque()
    q.append(root)
    while(len(q)>0):
        node=q.popleft()
        print(node.data)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(55)
root.left.right=Node(34)
root.right.right=Node(129)
Levelorder(root)
