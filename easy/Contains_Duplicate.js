/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let track = {}
  for (let i = 0; i < nums.length; i++)
    if (track[nums[i]] === undefined) track[nums[i]] = 1
    else track[nums[i]] += 1

  let keysum = Object.values(track).reduce(
    (accumulator, currentValue) => accumulator + Number(currentValue),
    0
  )
  console.log(keysum, Object.keys(track).length, track)
  return keysum != Object.keys(track).length
}

let nums = [1, 2, 3, 1]

console.log(containsDuplicate(nums))
