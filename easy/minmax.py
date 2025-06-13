class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        if len(nums) == 1:
            print(nums[0])
            return nums[0]
        newNums = [0] * int(len(nums) / 2)
        # print(newNums)
        i = 0
        while i < len(newNums):
            # print(nums[i], end=" ")
            # print(i)
            if i % 2 == 0:
                newNums[i] = min(nums[2 * i], nums[2 * i + 1])
            else:
                newNums[i] = max(nums[2 * i], nums[2 * i + 1])
            i += 1
        # print(newNums)
        return self.minMaxGame(newNums)
    



s = Solution()

s.minMaxGame([1, 3, 5, 2, 4, 8, 2, 2])  
# Output: 1
s.minMaxGame([3])
# Output: 3
s.minMaxGame([1, 2, 3, 4])
# Output: 1
s.minMaxGame([1, 2, 3, 4, 5, 6, 7, 8])
# Output: 1
s.minMaxGame([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Output: 1
