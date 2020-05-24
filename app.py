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
        self.mousePos = None
        self.selected_box = None

    def run(self):
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
        self.drawborder()
        if self.selected_box:
            self.draw_selected_box(self.selected_box)
        pygame.display.update()

    def eventhandling(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(self.mousePos)
                if self.is_mouse_position_inside_grid(self.mousePos):
                    # print('Inside Grid')
                    self.selected_box = self.grid_index_based_on_selected_position(self.mousePos)
                    # print(self.selected_box[0])
                else:
                    # print('Outside Grid')
                    self.selected_box = None

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
        print(x_index)
        print(selectedPosition[0]/ROWSIZE)
        y_index = selectedPosition[1]//COLUMNSIZE
        print(y_index)
        print(selectedPosition[1] / COLUMNSIZE)
        return (x_index, y_index)

    def draw_selected_box(self, selected_box):
        rect = self.selected_box_rect(selected_box)
        pygame.draw.rect(self.window, BLUE, rect)

    def selected_box_rect(self, selected_box):
        x_cord = SIDE_MARGIN + selected_box[0]*ROWSIZE
        y_cord = TOP_MARGIN + selected_box[1]*COLUMNSIZE
        return pygame.Rect(x_cord, y_cord, ROWSIZE, COLUMNSIZE)