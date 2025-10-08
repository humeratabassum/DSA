class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]

        end=nums[0]

        for i in range(1,len(nums)):
            end=max(end+nums[i],nums[i])
            res=max(res,end)
        return res
        

        