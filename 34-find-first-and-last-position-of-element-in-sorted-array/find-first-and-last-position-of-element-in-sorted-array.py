class Solution(object):
    def searchRange(self, nums, target):
        def binarySearch(left):
            l,r=0,len(nums)-1
            index=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    index=mid
                    if left:
                        r=mid-1
                    else:
                        l=mid+1
            return index
        return [binarySearch(True),binarySearch(False)]

        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        