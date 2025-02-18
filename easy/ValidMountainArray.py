class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # Walk up the mountain (increasing phase)
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak can't be the first or last element
        if i == 0 or i == n - 1:
            return False

        # Walk down the mountain (decreasing phase)
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        # If we reached the end, it's a valid mountain
        return i == n - 1


# Test cases
arr1 = [0, 3, 2, 1]
arr2 = [0, 2, 3, 3, 2, 1]
arr3 = [0, 1, 2, 3, 4, 5]
arr4 = [5, 4, 3, 2, 1]
arr5 = [0, 1, 2, 1, 0]

print(Solution().validMountainArray(arr1))  # True
print(Solution().validMountainArray(arr2))  # False (plateau)
print(Solution().validMountainArray(arr3))  # False (only increasing)
print(Solution().validMountainArray(arr4))  # False (only decreasing)
print(Solution().validMountainArray(arr5))  # True
