# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Left → Node → Right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev=None
        self.count=0
        self.max=0
        self.mode=[]

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev==node.val:
                self.count+=1
            else:
                self.count=1
                self.prev=node.val
            
            if self.count>self.max:
                self.max=self.count
                self.mode=[node.val]
            
            elif self.count==self.max:
                self.mode.append(node.val)

            inorder(node.right)
        inorder(root)
        return self.mode






        # self.prev=None
        # self.count=0
        # self.max=0
        # self.mode=[]

        # def inorder(node):
        #     if not node:
        #         return
            
        #     inorder(node.left)

        #     if self.prev==node.val:
        #         self.count+=1
        #     else:
        #         self.count=1
        #         self.prev=node.val
            
        #     if self.count>self.max:
        #         self.max=self.count
        #         self.mode=[node.val]
            
        #     elif self.count==self.max:
        #         self.mode.append(node.val)
            
        #     inorder(node.right)
        # inorder(root)
        # return self.mode




        