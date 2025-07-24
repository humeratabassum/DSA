"""
Explanation:
The list is already sorted.

We use two pointers:

i tracks the position of the last unique element.

j scans the array.

When we find a new unique value, we increment i and place that unique value at nums[i].
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return False
        
        i=0

        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1