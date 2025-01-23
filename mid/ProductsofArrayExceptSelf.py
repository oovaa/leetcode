import math


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        hold = math.prod(nums)
        return [round(hold / x) if x != 0 else 0 for x in nums]


nums = [-1, 0, 1, 2, 3]

print(Solution().productExceptSelf(nums))




# import math


# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         zero_count = nums.count(0)
#         if zero_count > 1:
#             return [0] * len(nums)
#         elif zero_count == 1:
#             product = 1
#             zero_index = None
#             for i, x in enumerate(nums):
#                 if x != 0:
#                     product *= x
#                 else:
#                     zero_index = i
#             result = [0] * len(nums)
#             result[zero_index] = product
#             return result
#         else:
#             hold = math.prod(nums)
#             return [round(hold / x) for x in nums]


# nums = [-1, 0, 1, 2, 3]

# print(Solution().productExceptSelf(nums))
