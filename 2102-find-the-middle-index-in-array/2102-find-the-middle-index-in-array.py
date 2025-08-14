class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left=0
        total_sum=sum(nums)

        for i in range(len(nums)):
            left+=nums[i]

            if left==total_sum:
                return i
            
            total_sum-=nums[i]
        return -1

        