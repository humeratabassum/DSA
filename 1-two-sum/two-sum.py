"""          BRUTE FORCE
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return False
"""
"""OPTIMAL  Solution using hasmap / dictionary"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map={}    #dictionary (numbers:indices)
        for i,num in enumerate(nums):
            diff=target-num
            if diff in h_map:
                return [i,h_map[diff]]
            h_map[num]=i   #add current number and value in h_map if it doesnt exist
        return False

