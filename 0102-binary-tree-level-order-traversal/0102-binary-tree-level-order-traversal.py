# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #If the tree is empty (no root), return an empty list.
        if not root:
            return []
        
        result=[]
        queue=deque([root])     #BFS used a queeue , start with root in queue

        while queue:
            level=[]
            size=len(queue)

            for _ in range(size):
                node=queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result




        