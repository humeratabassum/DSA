class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1   # Start with the full range of the array

        while l<r:
            mid=(l+r)//2

            # mid ^ 1 gives the index of the pair:
            # If mid is even → mid ^ 1 = mid + 1
            # If mid is odd  → mid ^ 1 = mid - 1

            if nums[mid]==nums[mid^1]:
                l=mid+1
            else:
                r=mid
         # When l == r, we've found the single non-duplicate element
        return nums[l]





        