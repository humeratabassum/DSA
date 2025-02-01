class Solution(object):
    def maxDepth(self, s):
        current_depth=0
        result=0
        for char in s:
            if char=="(":
                current_depth+=1
            elif char==")":
                current_depth-=1
            result=max(result,current_depth)
        return result
        """
        :type s: str
        :rtype: int
        """
        