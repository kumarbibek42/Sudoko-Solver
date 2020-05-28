from config import *
import pygame
import sys


class App:
    def __init__(self):
        print("initialized")
        pygame.init()
        pygame.display.set_caption(APP_TITLE)
        self.window = pygame.display.set_mode((HIGHT, WIDTH))
        self.running = True
        self.gridData = grid_num_array
        self.mousePos = None
        self.selected_box = None
        self.font = pygame.font.SysFont("arial", COLUMNSIZE//2)
        self.disabledCells = set()
        self.empty_cells = []

    def run(self):
        self.load_disabled_cells()
        while self.running:
            self.eventhandling()
            self.update()
            self.drawing()
        pygame.quit()
        sys.exit()

    def update(self):
        self.mousePos = pygame.mouse.get_pos();

    def drawing(self):
        self.window.fill(WHITE)
        if self.selected_box:
            self.draw_selected_box(self.selected_box)
        self.draw_numbers_to_the_grid()
        self.drawborder()
        pygame.display.update()

    def eventhandling(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousePos = event.pos;
                if self.is_mouse_position_inside_grid(self.mousePos):
                    selected_cell = self.grid_index_based_on_selected_position(self.mousePos)
                    if self.is_editable_cell(selected_cell):
                        self.selected_box = self.grid_index_based_on_selected_position(self.mousePos)
                    else:
                        self.selected_box = None
                else:
                    self.selected_box = None
            if event.type == pygame.KEYDOWN:
                if self.selected_box and self.is_editable_cell(self.selected_box):
                    if event.unicode.isnumeric():
                        self.gridData[self.selected_box[1]][self.selected_box[0]] = int(event.unicode)
                        if self.is_all_empty_cells_filled():
                            print('All filled')
                            self.is_sudoko_solved()

    def drawborder(self):
        # pygame.draw.line(self.window, BLACK, (SIDE_MARGIN, TOP_MARGIN), (WIDTH - SIDE_MARGIN, TOP_MARGIN), THICKLINEWIDTH)
        rect = pygame.Rect(SIDE_MARGIN, TOP_MARGIN, WIDTH - 2*SIDE_MARGIN, HIGHT - 2*TOP_MARGIN)
        for i in range(1, 9):
            defaultThickness = 1
            if i%3 == 0:
                defaultThickness = THICKLINEWIDTH
            pygame.draw.line(self.window, BLACK, (SIDE_MARGIN + i*ROWSIZE, TOP_MARGIN),
                             (SIDE_MARGIN + i*ROWSIZE, HIGHT - TOP_MARGIN), defaultThickness)
            pygame.draw.line(self.window, BLACK, (SIDE_MARGIN, SIDE_MARGIN + i*ROWSIZE),
                             (WIDTH - SIDE_MARGIN, SIDE_MARGIN + i*ROWSIZE), defaultThickness)
        pygame.draw.rect(self.window, BLACK, rect, THICKLINEWIDTH)

    def is_mouse_position_inside_grid(self, position):
        x_position = position[0]
        y_position = position[1]
        if ((x_position > MIN_GRID_X_POSITION) and (x_position < MAX_GRID_X_POSITION) and
                (y_position > MIN_GRID_Y_POSITION) and (y_position < MAX_GRID_Y_POSITION)):
            return True
        return False

    def grid_index_based_on_selected_position(self, selectedPosition):
        x_index = selectedPosition[0]//ROWSIZE
        y_index = selectedPosition[1]//COLUMNSIZE
        return (x_index, y_index)

    def draw_selected_box(self, selected_box):
        rect = self.get_selected_box_rect(selected_box)
        pygame.draw.rect(self.window, BLUE, rect)

    def draw_disabled_box(self, selected_box):
        rect = self.get_selected_box_rect(selected_box)
        pygame.draw.rect(self.window, GRAY, rect)

    def get_selected_box_rect(self, selected_box):
        x_cord = SIDE_MARGIN + selected_box[0]*ROWSIZE
        y_cord = TOP_MARGIN + selected_box[1]*COLUMNSIZE
        return pygame.Rect(x_cord, y_cord, ROWSIZE, COLUMNSIZE)

    def add_text_content(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        font_width = font.get_width()
        font_height = font.get_height()
        pos = ((pos[0] + (COLUMNSIZE - font_width)//2), (pos[1] + (COLUMNSIZE - font_height)//2))
        window.blit(font, pos)

    def get_text_position(self, pos_index):
        x_pos = pos_index[1]*COLUMNSIZE + TOP_MARGIN
        y_pos = pos_index[0]*COLUMNSIZE + TOP_MARGIN
        return (x_pos, y_pos)

    def draw_numbers_to_the_grid(self):
        for i, row in enumerate(self.gridData):
            for j, cellValue in enumerate(row):
                if cellValue != 0:
                    blocked_cell_key = str(i) + str(j)
                    if blocked_cell_key in self.disabledCells:
                        self.draw_disabled_box((j, i))
                    self.add_text_content(self.window, str(cellValue), self.get_text_position((i, j)))

    def is_editable_cell(self, selected_cell):
        cellKey = str(selected_cell[1])+str(selected_cell[0])
        if cellKey in self.disabledCells:
            return False
        return True

    def load_disabled_cells(self):
        for i, row in enumerate(self.gridData):
            for j, cellValue in enumerate(row):
                if cellValue != 0:
                    blocked_cell_key = str(i) + str(j)
                    self.disabledCells.add(blocked_cell_key)
                else:
                    self.empty_cells.append((i, j))

    def is_all_empty_cells_filled(self):
        for tup in self.empty_cells:
            if self.gridData[tup[0]][tup[1]] == 0:
                return False
        return True

    def is_sudoko_solved(self):
        verify_solved(self.gridData)