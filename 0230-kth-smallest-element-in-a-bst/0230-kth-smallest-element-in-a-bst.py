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
        self.count=0     # Initialize count of nodes visited so far
        self.result=None   # Initialize the variable to store k-th smallest value



        def inorder(node):
            if not node:        # If current node is None
                return None

            inorder(node.left)  # Step 1: Traverse the left subtree

            self.count+=1      # Step 2: Visit current node, increment count by 1
            if self.count==k:
                self.result=node.val
                return   # Stop further traversal once we found the k-th smallest
            inorder(node.right) # Step 4: Traverse the right subtree
        
        inorder(root)    # Start in-order traversal from root

        return self.result  # Return the k-th smallest element found

        




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

        