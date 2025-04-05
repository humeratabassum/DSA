# # class Solution(object):
# #     def search(self, nums, target):
# #         low, high = 0, len(nums) - 1

# #         while low <= high:
# #             mid = (low + high) // 2

# #             if nums[mid] == target:
# #                 return True 
# #                  # Target found
# #             if nums[low]<=nums[mid]:
# #                 if nums[low]<=target<nums[mid]:
# #                     high=mid-1
# #                 else:
# #                     low=mid+1
# #             else:
# #                 if nums[mid]<target<nums[high]:
# #                     low=mid+1
# #                 else:
# #                     high=mid-1
# #         return False

# class Solution(object):
#     def search(self, nums, target):
#         low, high = 0, len(nums) - 1

#         while low <= high:
#             mid = (low + high) // 2

#             if nums[mid] == target:
#                 return True  # Or return mid if index is required

#             # Left part is sorted
#             if nums[low] <= nums[mid]:
#                 if nums[low] <= target < nums[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1

#             # Right part is sorted
#             else:
#                 if nums[mid] < target <= nums[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1

#         return False

class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid  # Target found, return index

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target in left
                else:
                    left = mid + 1   # Target in right

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target in right
                else:
                    right = mid - 1  # Target in left

        return -1  # Not found
      