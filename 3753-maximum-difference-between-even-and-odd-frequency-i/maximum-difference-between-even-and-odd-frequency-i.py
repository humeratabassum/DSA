# Given a lowercase string `s`
# Find:
#    maxOdd → Maximum frequency among characters that occur an odd number of times
#    minEven → Minimum frequency among characters that occur an even number of times
# Return: maxOdd - minEven

from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:        # Step 1: Count frequencies of each character
        # #frequency-count
        freq=Counter(s)

        max_odd=0
        min_even=len(s)  #for calculation min even we need comparision so we look len(s)

        for char in freq.values():
            if char%2==1:
                max_odd=max(max_odd,char)                #odd
            else:
                min_even=min(min_even,char)             #even
        return max_odd-min_even

        