class Solution:
    def secondsToRemoveOccurrences(self, s):
        seconds = zeros = 0
        for char in s:
            if char == "0":
                zeros += 1
            elif zeros:  # char == '1'
                seconds = max(seconds + 1, zeros)
        return seconds


s = "0110101"
print(Solution().secondsToRemoveOccurrences(s))
