class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        l=0
# Step 3: Loop through each index
# Add current number to left sum

        for i in range(len(nums)):
            l+=nums[i]

            if l==total_sum:
                return i
# Step 5: Reduce current number from total sum            
            total_sum-=nums[i]
        
        return -1
        