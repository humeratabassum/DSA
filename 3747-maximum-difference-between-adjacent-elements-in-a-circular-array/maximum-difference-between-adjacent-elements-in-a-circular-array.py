class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxdiff=abs(nums[-1]-nums[0])

        for i in range(len(nums)-1):
            diff=abs(nums[i]-nums[i+1])
            
            maxdiff=max(diff,maxdiff)
        return maxdiff
        