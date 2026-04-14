import math
class Solution:
    """
    Row cannot have duplicates (array)
    Column cannot have duplicates (same index positions)
    Squares cannot have duplicates (slices of 3 across and down)
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_map_columns={}
        sudoku_map_squares={}
        for i,row in enumerate(board):
            row_arr=[]
            for j,tile in enumerate(row):
                if tile!='.':
                    square_num=f"{math.floor(j/3)}-{math.floor(i/3)}"
                    print({"i":i,"j":j, "square_num":square_num, "tile":tile})
                    if f"{square_num}" in sudoku_map_squares and tile in sudoku_map_squares[f"{square_num}"]:
                        print(f"first i:{i} j:{j} tile:{tile} arr:{sudoku_map_squares}")
                        return False
                    if j in sudoku_map_columns and tile in sudoku_map_columns[j]:
                        print(f"second {tile} {sudoku_map_columns}")
                        return False
                    if tile in row_arr:
                        print(f"third {tile} {row_arr}")
                        return False
                    row_arr.append(tile)
                    sudoku_map_columns[j] = sudoku_map_columns.get(j, []) + [tile]
                    sudoku_map_squares[f"{square_num}"]=sudoku_map_squares.get(f"{square_num}",[]) + [tile]
        print(sudoku_map_columns)
        print(sudoku_map_squares)
        return True

