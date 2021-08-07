from sys import *
from pygame.locals import *
import pygame
from tools import *


class Game:
    def __init__(self):
        self.title = GameTitle
        self.width = WIDTH
        self.height = HEIGHT
        self.row = ROW
        self.column = COLUMN
        self.mode = MODE
        if self.mode == 1:
            self.piece = [1, 2]
        else:
            self.piece = [1]
        self.screen = None
        self.board = board
        self.init_pygame()
        self.init_map()
        self.update()

    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.screen.fill(Wheat)

    def init_map(self):
        draw(self.screen, self.board)

    def update(self):
        while True:
            self.event_handler()
            pygame.display.update()

    def Game_over(self, color):
        if color == 1:
            self.screen.fill(Black)
        if color == 3:
            self.screen.fill(white)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                x, y = -1, -1
                for item in position_map.keys():
                    if event.pos[0] in item:
                        x = position_map[item]
                    if event.pos[1] in item:
                        y = position_map[item]
                if self.mode == 1:
                    self.board[x][y] = event.button
                draw(self.screen, self.board)
                if check_board(self.board) == 1:
                    self.Game_over(1)
                if check_board(self.board) == 3:
                    self.Game_over(3)
