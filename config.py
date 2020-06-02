from math import sqrt
from services import board_service
WINDOW_WIDTH = 600
WINDOW_HIGHT = 600
HIGHT = 600
WIDTH = 600
APP_TITLE = 'Sudoko Solver'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 111, 168)
GRAY = (202, 204, 207)
RED = (204, 22, 47)
GREEN = (25, 148, 35)
TOP_MARGIN = 12
SIDE_MARGIN = 12
THICKLINEWIDTH = 3
ROWSIZE = (HIGHT - 2 * TOP_MARGIN) // 9
COLUMNSIZE = (HIGHT - 2 * TOP_MARGIN) // 9
MIN_GRID_X_POSITION = SIDE_MARGIN
MAX_GRID_X_POSITION = WIDTH - SIDE_MARGIN
MIN_GRID_Y_POSITION = TOP_MARGIN
MAX_GRID_Y_POSITION = HIGHT - TOP_MARGIN
DIFFICULTY_LEVEL = 1
try:
    grid_num_array = board_service.get_board(DIFFICULTY_LEVEL)
except:
    grid_num_array = [
        [3, 1, 0, 5, 7, 8, 4, 9, 2],
        [5, 2, 9, 1, 3, 4, 7, 6, 8],
        [4, 8, 7, 6, 2, 9, 5, 3, 1],
        [2, 6, 3, 4, 1, 5, 9, 8, 7],
        [9, 7, 4, 8, 6, 3, 1, 2, 5],
        [8, 5, 1, 7, 9, 2, 6, 4, 3],
        [1, 3, 8, 9, 4, 7, 2, 5, 6],
        [6, 9, 2, 3, 5, 1, 8, 7, 4],
        [7, 4, 5, 2, 8, 6, 3, 1, 9]
    ]
ai_solved_grid = []
sudoko_size = 3 * 3
print(grid_num_array)


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


def is_box_correct(grid, indx, indy, n):
    visited_num = set()
    start_pos_of_box = (indx * n, indy * n)
    for i in range(n):
        for j in range(n):
            current_elem = grid[start_pos_of_box[0] + i][start_pos_of_box[1] + j]
            if current_elem in visited_num:
                return False
            visited_num.add(current_elem)
    return True


def is_all_boxes_correct(grid):
    n = int(sqrt(sudoko_size))
    for indx in range(n):
        for indy in range(n):
            if not is_box_correct(grid, indx, indy, n):
                return False
    return True


def is_all_rows_and_columns_valid(grid):
    for i in range(sudoko_size):
        if is_row_correct(grid, i) == False or is_column_correct(grid, i) == False:
            return False
    return True


def verify_solved(grid):
    return is_all_rows_and_columns_valid(grid) and is_all_boxes_correct(grid)


def is_row_assignment_correct(row_ind, num):
    if num in ai_solved_grid[row_ind]:
        return False
    return True


def is_column_assignment_correct(column_ind, num):
    for i in range(sudoko_size):
        if num == ai_solved_grid[i][column_ind]:
            return False
    return True


def is_box_assignment_correct(row_ind, column_ind, num):
    n = int(sqrt(sudoko_size))
    start_row_ind = row_ind - row_ind % n
    start_column_ind = column_ind - column_ind % n
    for i in range(n):
        for j in range(n):
            if num == ai_solved_grid[start_row_ind + i][start_column_ind + j]:
                return False
    return True


def is_assignment_safe(row_ind, column_ind, num):
    return is_row_assignment_correct(row_ind, num) and is_column_assignment_correct(column_ind, num) \
           and is_box_assignment_correct(row_ind, column_ind, num)


def initialize_solved_grid():
    for row in grid_num_array:
        current_row = []
        for val in row:
            current_row.append(val)
        ai_solved_grid.append(current_row)


def is_any_cell_empty(empty_cell):
    for i in range(sudoko_size):
        for j in range(sudoko_size):
            if ai_solved_grid[i][j] == 0:
                empty_cell[0] = i
                empty_cell[1] = j
                return True
    return False


def solve_sudoko():
    empty_cell = [0, 0]
    if not is_any_cell_empty(empty_cell):
        return True
    for num in range(1, sudoko_size+1):
        row_ind = empty_cell[0]
        column_ind = empty_cell[1]
        if is_assignment_safe(row_ind, column_ind, num):
            ai_solved_grid[row_ind][column_ind] = num
            if solve_sudoko():
                return True
            ai_solved_grid[row_ind][column_ind] = 0
    return False


def solve_sudoko_using_backtracking():
    print(grid_num_array)
    initialize_solved_grid()
    res = solve_sudoko()
    print('Solved by backtracking:{}'.format(res))

def index_util(x_index, y_index):
    return str(x_index) + str(y_index)