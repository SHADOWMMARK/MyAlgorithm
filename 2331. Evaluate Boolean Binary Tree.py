def evaluateTree(self, root: Optional[TreeNode]) -> bool:
    def pGo(node):
        if node.val == 2:
            return pGo(node.left) or pGo(node.right)
        elif node.val == 3:
            return pGo(node.left) and pGo(node.right)
        else:
            return node.val
    ans = pGo(root)
    return ans
