class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create hash sets to track seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                # Skip empty cells
                if num == '.':
                    continue
                
                # Calculate which 3x3 box this cell belongs to
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check if number already exists in row, col, or box
                if num in rows[r] or num in cols[c] or num in boxes[box_idx]:
                    return False
                
                # Add number to the corresponding sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)
        
        return True