class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
    
def preOrderTraversal(root):
    if root==None:
        return
    else:
        print(root.data)
        preOrderTraversal(root.leftchild)
        preOrderTraversal(root.rightchild)

def inorderTraversal(root):
    if root == None:
        return
    else:
        inorderTraversal(root.leftchild)
        print(root.data)
        inorderTraversal(root.rightchild)

def postorderTraversal(root):
    if root == None:
        return
    else:
        postorderTraversal(root.leftchild)
        postorderTraversal(root.rightchild)
        print(root.data)
    
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
print("preorder")
preOrderTraversal(root)
print("inorder")
inorderTraversal(root)
print("postorder")
postorderTraversal(root)
print("size of tree")
print(sizetree(root))
