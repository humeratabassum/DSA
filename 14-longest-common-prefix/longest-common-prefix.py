class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str=min(strs)
        max_str=max(strs)
        res=""

        for i in range(len(min_str)):
            if min_str[i]==max_str[i]:
                res+=min_str[i]
            else:
                return res
        return res

        