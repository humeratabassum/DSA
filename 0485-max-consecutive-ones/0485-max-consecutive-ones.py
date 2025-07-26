class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count=0
        max_1=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                i+=1
            else:
                count=0
        
            max_1=max(max_1,count)
        return max_1