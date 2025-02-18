class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if not any(str(n) in row for n in range(1, 10)):
                return False
        for col in range(9):
            for i in range(9):
                print(board[col][i])


board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


print(Solution().isValidSudoku(board))

# Output: true
