function areSetsEqual(set1, set2) {
  if (set1.size !== set2.size) return false
  for (let item of set1) {
    if (!set2.has(item)) return false
  }
  return true
}

// Example usage
const setA = new Set([1, 2, 3])
const setB = new Set([3, 2, 1])
console.log(areSetsEqual(setA, setB)) // Output: true
