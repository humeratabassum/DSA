# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         result=[]

#         for i in range(len(nums)-2):
#             if i>0 and nums[i]==nums[i-1]:
#                 continue      
            
#             left,right=i+1,len(nums)-1

#             while left<right:
#                 total=nums[i]+nums[left]+nums[right]

#                 if total==0:
#                     result.append(nums[i]+nums[left]+nums[right])

#                     while left<right and nums[left]==nums[left+1]:
#                         left+=1
#                     while left <  right and nums[right]==nums[right-1]:
#                         right-=1
                    
#                     left+=1
#                     right-=1
                
#                 elif totl<0:
#                     left+=1
#                 else:
#                     right-=1
#         return result

class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the array
        result = []

        for i in range(len(nums) - 2):  # Step 2: Iterate through the array
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for i
                continue

            left, right = i + 1, len(nums) - 1  # Step 3: Two-pointer approach

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:  # Found a valid triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # Move pointers and skip duplicate values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif total < 0:  # Increase sum
                    left += 1
                else:  # Decrease sum
                    right -= 1
        
        return result

