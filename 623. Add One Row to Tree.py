"""
1. if depth == 1, means need to add a root node and make the old root node as its left child.
2. Using BFS to find nodes layer by layer, when reach the certain layer (I use list named temp). 
then add new nodes between the layer.
3. Need to pay attention when nodes in temp at the certain layer having no child (as leaf nodes)
or only having one child (for example only have left child but no right child).
need to add a node using the input val, to the empty spots.
"""
def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        fake = root
        if depth == 1:
            new = TreeNode(val,root,None)
            return new
        temp = [root]
        k = 1
        while temp and k < depth-1:
            k += 1
            ntemp = []
            for n in temp:
                if n.left:
                    ntemp.append(n.left)
                if n.right:
                    ntemp.append(n.right)
            temp = ntemp

        for n in temp:
            if n.left:
                old = n.left
                new = TreeNode(val)
                n.left = new
                new.left = old
            else:
                new = TreeNode(val)
                n.left = new
            if n.right:
                old = n.right
                new = TreeNode(val)
                n.right = new
                new.right = old
            else:
                n.right = TreeNode(val)
        return fake
        
