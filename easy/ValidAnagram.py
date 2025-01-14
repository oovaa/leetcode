class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {char: s.count(char) for char in s}
        dt = {char: t.count(char) for char in t}
        return ds == dt


s = "racecar"
t = "carrace"

sol = Solution()


print(sol.isAnagram(t, s))
