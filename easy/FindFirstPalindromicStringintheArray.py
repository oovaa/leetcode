class Solution:
    def check_word(self, word: str):
        begin_index, end_index = 0, len(word) - 1
        while begin_index < end_index:
            if word[end_index] != word[begin_index]:
                return False
            begin_index += 1
            end_index -= 1
        return True

    def firstPalindrome(self, words: list[str]) -> str:
        for w in words:
            if self.check_word(w):
                return w

        return ""


words = ["abc","car","ada","racecar","cool"]

print(Solution().firstPalindrome(words))
