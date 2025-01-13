import math


def is_perfect_square(n):
    end = n
    start = 0

    while start <= end:
        mid = math.floor(start + (end - start) / 2)
        square = mid * mid
        if square == n:
            return True
        elif square > n:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == "__main__":
    print(is_perfect_square(10))  # expect False
    print(is_perfect_square(2025))  # expect True
    print(is_perfect_square(-1))  # expect False
