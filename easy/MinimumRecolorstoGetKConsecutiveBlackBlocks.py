class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        total_subs = len(blocks) - k + 1
        min_count = k

        for i in range(total_subs):
            hold = blocks[i : i + k]
            min_count = min(hold.count("W"), min_count)
            print(min_count)

        return min_count


blocks = "WBWBBBW"
k = 2


print(Solution().minimumRecolors(blocks, k))
