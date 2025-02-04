class Solution(object):
    def nextPermutation(self, nums):

        n = len(nums)
        i = n - 2

        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # Step 2: Find the number just larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # Swap

        # Step 3: Reverse the part after i
        nums[i + 1:] = reversed(nums[i + 1:])

        # """
        # :type nums: List[int]
        # :rtype: None Do not return anything, modify nums in-place instead.
        # """
        