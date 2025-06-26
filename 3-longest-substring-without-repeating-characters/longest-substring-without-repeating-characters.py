class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0    #left pointer
        seen=set()      #we use set to store unique values and check duplicates
        max_len=0           #to find  the ,max length

        for r in range(len(s)):     #r is another pointer in sliding window
            while s[r] in seen:      #if right side char is already in seen , then we will shrink window and update pointer
                seen.remove(s[l])
                l+=1
            
            seen.add(s[r])      #after removing element from winow , add right elt to seen 
            max_len=max(max_len,r-l+1)    
        return max_len


        