# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Root → Left → Right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        curr=[root.val]
        right=self.preorderTraversal(root.right)
        left=self.preorderTraversal(root.left)

        return curr+left+right

        