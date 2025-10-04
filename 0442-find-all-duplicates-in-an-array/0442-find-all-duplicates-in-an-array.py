class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen={}
        dup=[]

        for num in nums:
            if num in seen:
                dup.append(num)
            else:
                seen[num]=1
        return dup




        # dup=[]
        # for i in nums:

        #     i=abs(i)
        #     if nums[i-1]<0:
        #         dup.append(i)
        #     else:
        #         nums[i-1] *= -1
        # return dup

        