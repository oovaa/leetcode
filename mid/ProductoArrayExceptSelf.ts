function productExceptSelf(nums: number[]): number[] {
  const n = nums.length
  let left = 1
  let right = 1

  const lr: number[] = new Array(n).fill(0)
  const rr: number[] = new Array(n).fill(0)

  for (let i = 0; i < n; i++) {
    let j = n - i - 1

    lr[i] = left
    rr[j] = right
    left *= nums[i]
    right *= nums[j]
  }

  return lr.map((x, i) => x * rr[i])
}

console.log(productExceptSelf([1, 2, 3, 4]))
