class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".": continue
                sub_box = (i // 3) * 3 + (j // 3)
                if cell in rows[i] or cell in cols[j] or cell in sub_boxes[sub_box]:
                    return False
                rows[i].add(cell)
                cols[j].add(cell)
                sub_boxes[sub_box].add(cell)
                print(rows)
                print(cols)
                print(sub_boxes)
        return True
            