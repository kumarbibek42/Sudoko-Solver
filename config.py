import random

HIGHT = 600
WIDTH = 600
APP_TITLE = 'Sudoko Solver'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 111, 168)
GRAY = (62, 64, 66)
TOP_MARGIN = 12
SIDE_MARGIN = 12
THICKLINEWIDTH = 3
ROWSIZE = (HIGHT-2*TOP_MARGIN)//9
COLUMNSIZE = (HIGHT-2*TOP_MARGIN)//9
MIN_GRID_X_POSITION = SIDE_MARGIN
MAX_GRID_X_POSITION = WIDTH - SIDE_MARGIN
MIN_GRID_Y_POSITION = TOP_MARGIN
MAX_GRID_Y_POSITION = HIGHT - TOP_MARGIN
grid_num_array = []
sudoko_size = 3*3
for i in range(sudoko_size):
    rows = []
    for j in range(sudoko_size):
        rows.append(random.randint(0, 9))
    grid_num_array.append(rows)
print(grid_num_array)