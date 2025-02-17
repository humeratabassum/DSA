class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        