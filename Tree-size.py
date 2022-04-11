
// Tree size of binary tree..

class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
    
def sizetree(root):
    if root == None:
        return 0
    else:
        ls=sizetree(root.leftchild)
        rs=sizetree(root.rightchild)
        return ls+rs+1

root=Node(10)
root.leftchild=Node(20)
root.rightchild=Node(5)
root.leftchild.rightchild=Node(100)
root.leftchild.leftchild=Node(4)
print("size of tree")
print(sizetree(root))
