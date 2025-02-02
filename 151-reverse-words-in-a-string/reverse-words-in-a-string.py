class Solution(object):
    def reverseWords(self, s):
        return " ".join(reversed(s.split()))
        """
        :type s: str
        :rtype: str
        """
        