class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hold = {}
        for str in strs:
            sorted_word = "".join(sorted(str))
            if hold.get(sorted_word, False):
                hold[sorted_word].append(str)
            else:
                hold[sorted_word] = [str]
        return list(hold.values())

        # hold = {}
        # for str in strs:
        #     cascii = sum([ord(i) for i in str])
        #     print(str, cascii)
        #     present = hold.get(cascii, False)
        #     if not present:
        #         hold[cascii] = [str]
        #     else:
        #         hold.get(cascii).append(str)

        # return list(hold.values())


# strs = ["act", "pots", "tops", "cat", "stop", "hat"]
# strs =['x']
strs = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]


print(Solution().groupAnagrams(strs))
