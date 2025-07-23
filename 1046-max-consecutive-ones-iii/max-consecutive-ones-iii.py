class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                k-=1    #use a flip
            if k<0:            #if available k are less then we shrink using left pointer
                if nums[l]==0:
                    k+=1            #if l==0 , update k . add 1
                l+=1   #
        return r-l+1        #this returns max window l-r+1

            
        