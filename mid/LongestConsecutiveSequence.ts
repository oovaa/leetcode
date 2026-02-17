class Solution {
  /**
   * @param {number[]} nums
   * @return {number}
   */
  longestConsecutive(nums: number[]) {
    let ans = 0
    let hold: number[] = []
    let next_to_search
    for (let i = 0; i < nums.length; i++) {
      //   console.log('loop starts i = ', i, nums[i])
      hold = []
      hold.push(nums[i])
      next_to_search = nums[i] + 1
      //   console.log('next to search', next_to_search)

      while (nums.includes(next_to_search)) {
        // console.log('next found', next_to_search, 'hold', hold)
        hold.push(next_to_search)
        next_to_search++
      }
      ans = Math.max(ans, hold.length)
      //   console.log('ans', ans, 'hold', hold)
    }
    return ans
  }
}

const nums = [0, 3, 2, 5, 4, 6, 1, 1]

console.log(new Solution().longestConsecutive(nums))
