class Solution(object):
    def longestPalindrome(self, s):
        res=""
        reslength=0
        # odd case
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslength:
                    res=s[l:r+1]
                    reslength=r-l+1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslength:
                    res=s[l:r+1]
                    reslength=r-l+1
                l-=1
                r+=1
        return res



        """
        :type s: str
        :rtype: str
        """
        