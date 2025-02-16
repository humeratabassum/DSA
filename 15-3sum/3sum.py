
# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()  # Step 1: Sort the array
#         result = []

#         for i in range(len(nums) - 2):  # Step 2: Iterate through the array
#             if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for i
#                 continue

#             left, right = i + 1, len(nums) - 1  # Step 3: Two-pointer approach

#             while left < right:
#                 total = nums[i] + nums[left] + nums[right]

#                 if total == 0:  # Found a valid triplet
#                     result.append([nums[i], nums[left], nums[right]])

#                     # Move pointers and skip duplicate values
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
                    
#                     left += 1
#                     right -= 1

#                 elif total < 0:  # Increase sum
#                     left += 1
#                 else:  # Decrease sum
#                     right -= 1
        
#         return result

class Solution:
    def threeSum(self, nums):
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output