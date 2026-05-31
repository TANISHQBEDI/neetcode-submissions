class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for a valid rows
        for row in range(9):
            seen = set()
            for col in range(9):
                curr = board[row][col]
                if curr != '.':
                    if curr in seen:
                        return False
                    seen.add(curr)
        # Check for a valid cols
        for row in range(9):
            seen = set()
            for col in range(9):
                curr = board[col][row]
                if curr != '.':
                    if curr in seen:
                        return False
                    seen.add(curr)
        # Check for valid sub-box
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        curr = board[box_row * 3 + row][box_col * 3 + col]
                        if curr != '.':
                            if curr in seen:
                                return False
                            seen.add(curr)

        return True