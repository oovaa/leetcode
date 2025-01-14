class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {l: s.count(l) for l in s}
        dt = {l: t.count(l) for l in t}
        return ds == dt


s = "racecar"
t = "carrace"

sol = Solution()


print(sol.isAnagram(t, s))
