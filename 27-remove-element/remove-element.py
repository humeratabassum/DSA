"""
How It Works (Step-by-Step):
k keeps track of the next position to place a value that is NOT equal to val.

Loop through each element:

If nums[i] != val, copy it to nums[k], and move k forward.



"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
        