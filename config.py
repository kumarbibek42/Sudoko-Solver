import random

HIGHT = 600
WIDTH = 600
APP_TITLE = 'Sudoko Solver'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 111, 168)
GRAY = (202, 204, 207)
TOP_MARGIN = 12
SIDE_MARGIN = 12
THICKLINEWIDTH = 3
ROWSIZE = (HIGHT-2*TOP_MARGIN)//9
COLUMNSIZE = (HIGHT-2*TOP_MARGIN)//9
MIN_GRID_X_POSITION = SIDE_MARGIN
MAX_GRID_X_POSITION = WIDTH - SIDE_MARGIN
MIN_GRID_Y_POSITION = TOP_MARGIN
MAX_GRID_Y_POSITION = HIGHT - TOP_MARGIN
grid_num_array = [
    [ 0, 1, 6, 5, 7, 8, 4, 9, 2 ],
    [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
    [ 0, 8, 7, 6, 2, 9, 5, 3, 1 ],
    [ 2, 6, 3, 4, 1, 5, 9, 8, 7 ],
    [ 9, 7, 4, 8, 6, 3, 1, 2, 5 ],
    [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
    [ 1, 3, 8, 9, 4, 7, 2, 5, 6 ],
    [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
    [ 7, 4, 5, 2, 8, 6, 3, 1, 9 ]
]
sudoko_size = 3*3

# for i in range(sudoko_size):
#     rows = []
#     for j in range(sudoko_size):
#         rows.append(random.randint(0, 9))
#     grid_num_array.append(rows)
print(grid_num_array)


def solve_sudoko_using_backtracking():
    print('AI work')


def is_row_correct(grid, row_index):
    visited_num = set()
    for val in grid[row_index]:
        if val in visited_num:
            return False
        visited_num.add(val)
    return True


def is_column_correct(grid, column_index):
    visited_num = set()
    for ind in range(sudoko_size):
        val = grid[ind][column_index]
        if val in visited_num:
            return False
        visited_num.add(val)
    return True


def is_all_rows_and_columns_valid(grid):
    for i in range(sudoko_size):
        if is_row_correct(grid, i) == False or is_column_correct(grid, i) == False:
            return False
    return True


def verify_solved(grid):
    res = is_all_rows_and_columns_valid(grid);
    print(res)
    return res
