function returnToBoundaryCount(nums: number[]): number {
  let ans = 0
  let hold = 0

  for (let i = 0; i < nums.length; i++) {
    hold += nums[i]
    if (hold == 0) ans++
  }

  return ans
}

console.log(returnToBoundaryCount([3, 2, -3, -4]))
