class Solution:
    def countLargestGroup(self, n: int) -> int:
        nl = list(range(n + 1))[1:]
        ans = {}
        for i in nl:
            holdd = list(x for x in str(i))
            s = sum([int(x) for x in holdd])
            ans[s] = ans.get(s, 0) + 1
        sizes = list(ans.values())
        # print(ans)
        return sizes.count(max(sizes))


n = 66

s = Solution()


print(s.countLargestGroup(n))
