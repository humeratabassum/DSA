"""
Key idea:

One half of the array (left or right) is always sorted.

Figure out which half is sorted, and whether the target lies in that half.

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
                    
            
















        # l,r=0,len(nums)-1
        

        # while l<=r:
        #     mid=(l+r)//2

        #     if nums[mid]==target:
        #         return mid
            
        #     if nums[l]<=nums[mid]:
        #         if nums[l]<=target<nums[mid]:
        #             r=mid-1
        #         else:
        #             l=mid+1
        #     else:
        #         if nums[mid]<target<=nums[r]:
        #             l=mid+1
        #         else:
        #             r=mid-1
        # return -1




        