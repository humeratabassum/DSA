class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if i==len(strs[j]) or strs[0][i]!=strs[j][i]:
                    return strs[j][:i]
        return strs[0]
        