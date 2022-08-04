    from collection import defaultdict
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        x=defaultdict(list)
        def r_side(node,h):
            if not node: return 
            x[h].append(node.val)
            r_side(node.left,h+1)
            r_side(node.right,h+1)
            
        r_side(root,0)
        
        return [v[0] for k,v in sorted(x.items())]
