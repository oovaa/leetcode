class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, v in enumerate(nums):
            hold = target - v
            nums[i] = None
            if hold in nums:
                return [i, nums.index(hold)]
            nums[i] = v
        return []


nums = [5, 5]
target = 10


sol = Solution()
print(sol.twoSum(nums, target))
