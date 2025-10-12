# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    def dfs(self,root):
        if not root:
            return 0
        return self.dfs(root.left)+self.dfs(root.right)+1
        