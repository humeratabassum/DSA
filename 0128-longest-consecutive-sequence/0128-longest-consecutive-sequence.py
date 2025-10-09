class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set=set(nums)
        longest=0

        for ele in num_set:
            if ele-1 not in num_set:
                curr=ele
                curr_len=1
            

                while curr+1 in num_set:
                    curr+=1
                    curr_len+=1
                
                longest=max(longest,curr_len)
        return longest

        