class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                
                num = board[i][j]
                
                if num == '.':
                    continue
                
                box_idx = (i // 3) * 3 + (j // 3)
                
                if num in row[i] or num in col[j] or num in boxes[box_idx]:
                    return False

                row[i][num] = True
                col[j][num] = True
                boxes[box_idx][num] = True

        return True