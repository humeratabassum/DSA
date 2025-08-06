class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(left):

            l,r=0,len(nums)-1
            index=-1

            while l<=r:
                mid=(l+r)//2

                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    index=mid       #target is found

                    if left:
                        r=mid-1
                    else:
                        l=mid+1
            return index

        return [binarysearch(True),binarysearch(False)]