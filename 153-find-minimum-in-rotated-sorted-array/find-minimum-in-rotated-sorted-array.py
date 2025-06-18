class Solution:
    def findMin(self, nums: List[int]) -> int:
        #irst find mid of the array to split it
        l,r=0,len(nums)-1
# compare the mid with right pointer
# 3, 4, 5, 1, 2
# l     m     r   
 #here mid>right , max elements are on left side so we place pointer towards the right 
#else right will move to mid eg:[11,12,13,15,17]

        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]
        