#it is easy just to use the BFS go over all the nodes in the same height of the tree.

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if root:
            temp = [root]
        else:
            return ans
        tempC = []
        while temp:
            vals = []
            for item in temp:
                vals.append(item.val)
                if item.children:
                    for i in item.children:
                        tempC.append(i) 
            ans.append(vals)
            vals = []
            temp = tempC
            tempC = []
        return ans
    
    
    def levelOrder2(self, root: 'Node') -> List[List[int]]:
        queue, res = [root], []
        while queue and queue[0]:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return res
