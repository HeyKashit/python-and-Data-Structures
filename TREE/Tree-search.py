
// searching in the binary tree 

class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

def search_bt(root,key):
    if root == None:
        return False
    if root.data == key:
        return True
    elif search_bt(root.left,key) == True:
        return True
    elif search_bt(root.right,key) == True:
        return True
    else:
        return False
      
root=Node(10)
root.leftchild=Node(20)
root.rightchild=Node(5)
root.leftchild.rightchild=Node(100)
root.leftchild.leftchild=Node(4)
root.rightchild.rightchild=Node(30)
root.rightchild.rightchild.rightchild=Node(120)
print(search_bt(root,5))
