# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        strs = []
        def helper(node,suf):
            nonlocal strs
            if not node.left and not node.right:
                strs.append(str(chr(int(node.val)+ord('a')))+suf)
                return
            if node.left:
                helper(node.left,str(chr(int(node.val)+ord('a')))+suf)
            if node.right:
                helper(node.right,str(chr(int(node.val)+ord('a')))+suf)
        helper(root,'')
        return min(strs)
