class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        started_decreesing = False

        # base case
        if len(arr) < 3:
            return False

        if arr[0] > arr[1]:
            return False

        for i, v in enumerate(arr):
            if i + 1 < len(arr):  # Check if arr[i+1] exists
                next = arr[i + 1]
                if v == next:
                    return False

                elif v > next:
                    started_decreesing = True

                if started_decreesing:
                    if v < next:
                        # print(
                        #     f"Returning False at index {i} because {v} is not less than {next}"
                        # )

                        return False
                else:
                    if v > next:
                        # print(
                        #     f"Returning False at index {i} because {v} is not greater than {next}"
                        # )
                        return False

            last = arr[len(arr) - 1]
            pre_last = arr[len(arr) - 2]

            if last > pre_last:
                print("last isnt larger than prelast")
                return False

        return True



arr = [0, 3, 2, 1]


print(Solution().validMountainArray(arr))
