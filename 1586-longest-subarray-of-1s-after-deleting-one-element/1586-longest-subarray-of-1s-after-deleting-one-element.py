class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n=len(nums)
        l=0
        zeros=0
        ans=0

        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            
            while zeros>1:
                if nums[l]==0:
                    zeros-=1
                l+=1
            
            ans=max(ans,r-l)
        return ans





        # n,l,zeros,ans=len(nums),0,0,0

        # for r,x in enumerate(nums):
        #     zeros+=(x==0)

        #     if zeros>1:
        #         zeros-=(nums[l]==0)
        #         l+=1
            
        #     ans=max(ans,r-l)
        # return ans



        