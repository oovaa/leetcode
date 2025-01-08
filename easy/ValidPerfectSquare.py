import math


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 1:
            return False
        start, end = 1, num

        while start <= end:
            mid = math.floor((start + end) / 2)
            sq = mid * mid

            if sq == num:
                return True
            elif sq > num:
                end = mid - 1
            else:
                start = mid + 1
        return False


sol = Solution()
print(sol.isPerfectSquare(9))
print("---------------------")
print(sol.isPerfectSquare(104976))
