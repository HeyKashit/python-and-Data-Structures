
// max element in the tree 

class Node:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

def max_element(root):
    if root==None:
        return 0
    else:
        lm=max_element(root.leftchild)
        rm=max_element(root.rightchild)
        return max(root.data,lm,rm)

root=Node(10)
root.leftchild=Node(20)
root.rightchild=Node(5)
root.leftchild.rightchild=Node(1005)
root.leftchild.leftchild=Node(4)

print("the max element")
print(max_element(root))
