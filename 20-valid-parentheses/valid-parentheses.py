"""
approach : use stack to remember brackets
when we find a closing bracket , we check if it matches the top of stack 
if it matches then pop it , else the string is not valid

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]            #TO KEEP TRACK OF OPENING BRACKETS
        pairs={")":"(","]":"[","}":"{"}     #mapiing closing to opening

        for char in s:
            if char in pairs:       #if it is closing bracket
                if not stack or stack[-1]!=pairs[char]:     #if top doesnt match and stack non emoty then not valid , return false
                    return False
                stack.pop()    #else it is valid so pop the opening present in stack
            else:
                stack.append(char)      #if it is opeming new one then append to stack
        if len(stack)==0:
            return True
        else:
            return False

            #if theres some leftover chars in stack then it is not valid so return False
            
        