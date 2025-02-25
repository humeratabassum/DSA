class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        s_to_t={}
        t_to_s={}

        for char_s,char_t in zip(s,t):
            if char_s in s_to_t and s_to_t[char_s]!=char_t:
                return False
            if char_t in t_to_s and t_to_s[char_t]!=char_s:
                return False
            
            s_to_t[char_s]=char_t
            t_to_s[char_t]=char_s
        return True



        # """
        # :type s: str
        # :type t: str
        # :rtype: bool
        # """
        