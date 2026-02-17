// @ts-ignore
class Solution {
  /**
   * @param {string} s
   * @return {boolean}
   */
  isPalindrome(s: string) {
    s = s
      .replaceAll(' ', '')
      .replaceAll(/[^a-z0-9]/gi, '')
      .toLocaleLowerCase()
    console.log(s)

    let start = 0,
      end = s.length - 1

    while (start < end) {
      if (s.charAt(start) != s.charAt(end)) {
        console.log(s.charAt(start), s.charAt(end))

        return false
      } else {
        start++
        end--
      }
    }
    return true
  }
}

console.log(new Solution().isPalindrome('Was it a car or a cat I saw?'))
