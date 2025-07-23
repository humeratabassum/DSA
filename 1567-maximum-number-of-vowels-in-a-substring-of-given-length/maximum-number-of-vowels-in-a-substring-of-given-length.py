class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set("aeiou")

        max_count=0
        curr_count=0

        # check for vowels count and step 2 : slide window

        for i in range(k):
            if s[i] in vowels:
                curr_count+=1
        max_count=max(curr_count,max_count)

        #slide the window
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                curr_count-=1
            if s[i] in vowels:
                curr_count+=1
            max_count=max(max_count,curr_count)
        return max_count

