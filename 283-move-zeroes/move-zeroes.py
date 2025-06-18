class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        #we need pos pointer to keep track of non zero elements 
        n=len(nums)
        pos=0

#if an element is non zero place it in pos pointer and increment 
        for i in range(n):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        
        #fill the non zeros
        while pos<n:
            nums[pos]=0
            pos+=1



        """
        Do not return anything, modify nums in-place instead.
        """
        