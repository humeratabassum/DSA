class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result=result^num   #xor operation 
        return result
        