class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=n*(n+1)//2
        return total_sum-sum(nums)



#this is brute force approach
"""        
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
        
"""
        