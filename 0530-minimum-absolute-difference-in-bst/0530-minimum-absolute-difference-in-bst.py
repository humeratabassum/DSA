# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)

        minval=float('inf')
        vals=inorder(root)
        for i in range(1,len(vals)):
            minval=min(minval,vals[i]-vals[i-1])
        return minval
        
        