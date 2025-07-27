class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for j in range(n):
            nums1[m+j]=nums2[j]
        nums1.sort()
""" APPROACH
You are given two sorted arrays:

nums1 of size m + n, where the first m elements are valid and the rest (n zeros) are placeholders.

nums2 of size n.


Your task is to merge nums2 into nums1 as one sorted array in-place.


"""







"""
        Do not return anything, modify nums1 in-place instead.
"""        """
        i=m-1
        j=n-1
        k=m+n-1

        while i>=0 and  j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
"""