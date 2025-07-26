class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result=result^num   #xor operation 
        return result
        
"""
| Step | `num` | `result = result ^ num` |Explanation                            |
| ---- | ----- | ----------------------- |-------------------------------------  |
| 1    | 4     | `0 ^ 4 = 4`             | First number                           
| 2    | 1     | `4 ^ 1 = 5`             | XOR with 1                            |
| 3    | 2     | `5 ^ 2 = 7`             | XOR with 2                            |
| 4    | 1     | `7 ^ 1 = 6`             | Cancels out 1 (since 1 appears twice) |
| 5    | 2     | `6 ^ 2 = 4`             | Cancels out 2                        
"""