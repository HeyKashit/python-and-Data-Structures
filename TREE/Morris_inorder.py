    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        result=[]
        while((root is not None)or(stack !=[])):
            while  root is not None:
                stack.append(root)
                root=root.left
            root = stack.pop()
            result.append(root.val)
            root=root.right
        return result
