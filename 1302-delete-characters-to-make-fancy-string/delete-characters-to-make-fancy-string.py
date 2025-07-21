class Solution:
    def makeFancyString(self, s: str) -> str:
        result=[]
        for char in s:
            if len(result)>=2 and result[-1]==char and result[-2]==char:
                continue            #there exists 2 consecutive vhars so we continue (ignore)
            result.append(char)
        return ''.join(result)
        