class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        ans=float('inf')
        l,t=0,0

        for r in range(n):
            t+=nums[r]
            while t>=target:
                ans=min(ans,r-l+1)
                t-=nums[l]
                l+=1
        return 0 if ans==float('inf') else ans
            
        