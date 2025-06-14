class Solution:
    def splitNum(self, num: int) -> int:
        n1, n2 = "", ""
        for i, d in enumerate(sorted(str(num))):
            if i % 2 == 0:
                n1 += d
            else:
                n2 += d
        # print(n1, n2)
        return int(n1) + int(n2)


s = Solution()


num = 4325

print(s.splitNum(num))
