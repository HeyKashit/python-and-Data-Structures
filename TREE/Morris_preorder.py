    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return
        stack = [root]
        result = []
        while(stack != []):
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
            
        return result
