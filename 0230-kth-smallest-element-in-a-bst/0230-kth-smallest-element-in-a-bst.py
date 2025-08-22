# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""BST + inorder traversal (Left → Node → Right) = sorted order.

So, if you list nodes by an inorder traversal, the k-th visited node is the answer."""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=0
        self.result=None

        def inorder(node):
            if not node:
                return None
            inorder(node.left)

            self.count+=1
            if self.count==k:
                self.result=node.val
                return
            inorder(node.right)
        inorder(root)
        return self.result

        




        # stack=[]
        # curr=root

        # while True:
        #     while curr:
        #         stack.append(curr)
        #         curr=curr.left
            
        #     curr=stack.pop()
        #     k-=1
        #     if k==0:
        #         return curr.val
        #     curr=curr.right

        