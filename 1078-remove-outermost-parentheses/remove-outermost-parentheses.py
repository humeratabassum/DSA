# class Solution(object):
#     def removeOuterParentheses(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        count = 0  # Keeps track of the depth of nesting
        
        for char in s:
            if char == '(':
                if count > 0:
                    result.append(char)  # Append only if it's not an outermost '('
                count += 1
            else:  # char == ')'
                count -= 1
                if count > 0:
                    result.append(char)  # Append only if it's not an outermost ')'
        
        return "".join(result)