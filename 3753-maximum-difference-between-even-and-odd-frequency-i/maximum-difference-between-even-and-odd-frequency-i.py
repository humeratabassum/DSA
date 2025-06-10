from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)

        max_odd=0
        min_even=len(s)

        for char in freq.values():
            if char%2==1:
                max_odd=max(max_odd,char)                #odd
            else:
                min_even=min(min_even,char)
        return max_odd-min_even

        