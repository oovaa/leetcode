class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # start with one letter
        wsize = 1
        cur, next = None, None

        # compare it with the next
        for index in range(len(s)):
            # print(s[index], index)
            cur = s[index : index + wsize]
            next = s[index + wsize : index + wsize + 1]
            if cur != next:
                index = 0
                print("in the if", index)
                wsize += 1

            print(cur, next)

        # if valid compare with the next
        # else increase the windwsize

    # if wo


slo = Solution()

slo.repeatedSubstringPattern("ababab")
