class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {x: nums.count(x) for x in nums}
        ans = []
        freq = [[] for _ in range(len(nums) + 1)]
        # print(count.items())
        for v, c in count.items():
            freq[c].append(v)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans


nums = [1, 2, 2, 3, 3, 3]
k = 2


print(Solution().topKFrequent(nums, k))
