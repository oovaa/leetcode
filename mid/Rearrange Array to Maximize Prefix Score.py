class Solution:
    def maxScore(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum > 0:
                count += 1
            else:
                break  # Since array is sorted descending, no point continuing

        return count


s = Solution()

nums = [2, -1, 0, 1, -3, 3, -3]
# nums = [-2, -3, 0]

print(s.maxScore(nums))
