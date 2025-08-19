class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map={}    #dictionary with {number : index map}

        for i,num in enumerate(nums):
            diff=target-num
            if diff in h_map:
                return [i,h_map[diff]]
            h_map[num]=i
        return False






        #brute force approach with n^2 TC
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        
        

        