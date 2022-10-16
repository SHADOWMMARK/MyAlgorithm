#include <unordered_map>
using namespace std;
// unordered_set<int> is like python's set()
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    unordered_set<int> s;
    bool findTarget(TreeNode* root, int k) {
        if(!root)return false;
        if(s.count(k - root->val))return true;
        s.insert(root->val);
        return findTarget(root->left,k) || findTarget(root->right,k);
    }
};
/*
this is the same function as the python way below:
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        stack,seen = [root],set()
        while stack:
            temp = stack.pop()
            if k-temp.val in seen:
                return True
            seen.add(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return False
*/