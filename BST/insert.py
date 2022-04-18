# BST insert...

class Bst:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

def insert(root,key):
    if root == None:
        return Bst(key)
    elif root.data == key:
        return root
    elif root.data > key:
        root.leftchild=insert(root.leftchild,key)
    else:
        root.rightchild=insert(root.rightchild,key)
    return "done"

def preorder(root):
    if root==None:
        return 0
    else:
        print(root.data)
        preorder(root.leftchild)
        preorder(root.rightchild)
 
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


newBST=Bst(30)
insert(newBST,20)
insert(newBST,40)
insert(newBST,15)
insert(newBST,100)
preorder(newBST)
