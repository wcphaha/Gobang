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
        # 通过正负1，对数字的取负数操作来实现黑白棋下棋切换
        self.piece = 1
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

    # 游戏结束
    def Game_over(self, color):
        if color == 1:
            self.screen.fill(Black)
        if color == -1:
            self.screen.fill(white)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                # 落子，改变棋盘
                drop_piece(self, event.pos)
                # 重新画棋盘
                draw(self.screen, self.board)
                # 判断本局是否结束
                if check_board(self.board) == 1:
                    self.Game_over(1)
                if check_board(self.board) == -1:
                    self.Game_over(-1)
