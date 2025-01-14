class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hold = {}

        for n in nums:
            hold[n] = hold.get(n, 0) + 1
            print(hold.get(n))
            if hold.get(n) != 1:
                return True
        return False


sol = Solution()

nums = [1, 2, 3, 3]

print(sol.hasDuplicate(nums))
