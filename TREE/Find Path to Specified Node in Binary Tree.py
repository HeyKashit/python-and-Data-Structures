class TreeNode:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

def path(root, k, l=[]):
    if not root:
        return []
    if root.val == k:
        return l

    # Pre-order traversal: Visit root, then left, then right.
    l.append(root.val)
    path(root.left, k, l)
    path(root.right, k, l)
    return l
    
    
    
# code run
>>> a = TreeNode(1)
>>> b = TreeNode(2)
>>> c = TreeNode(3)
>>> d = TreeNode(4)
>>> e = TreeNode(5)
>>> a.left = b
>>> a.right = c
>>> b.left = d
>>> b.right = e
>>> path(a, 4) # should be [1, 2, 4]
[1, 2, 5, 3]
