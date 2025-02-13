class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        max_product=nums[0]
        min_product=nums[0]
        result=nums[0]   
        for i in range(1,len(nums)):
            if nums[i]<0:
                max_product,min_product=min_product,max_product

            max_product=max(nums[i],nums[i]*max_product)
            min_product=min(nums[i],nums[i]*min_product)
            result=max(result,max_product)
        return result
 # if nums[i]<0:   #swap when encounter a neg number
            #     max_product,min_product=min_product,max_product



        