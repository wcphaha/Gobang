import pygame.draw
from constant import *


def drop_piece(self, pos):
    x, y = -1, -1
    for item in position_map.keys():
        if pos[0] in item:
            x = position_map[item]
        if pos[1] in item:
            y = position_map[item]
    if self.mode == 1:
        if self.board[x][y] == 0:
            self.board[x][y] = self.piece
            self.piece = -self.piece


# 判断是否形成5子
def check_board(board: list[list]):
    # 判断列
    for item in board:
        try:
            if str(item).index('-1, -1, -1, -1, -1'):
                return -1
        except ValueError:
            pass
        try:
            if str(item).index('1, 1, 1, 1, 1'):
                return 1
        except ValueError:
            pass
    # 先把矩阵转置一下
    tt = []
    for j in range(15):
        t = []
        for L in board:
            t.append(L[j])
        tt.append(t)
    # 判断行
    for item in tt:
        try:
            if str(item).index('-1, -1, -1, -1, -1'):
                return -1
        except ValueError:
            pass
        try:
            if str(item).index('1, 1, 1, 1, 1'):
                return 1
        except ValueError:
            pass
    # 将矩阵逆时针旋转一下
    tt = []
    for j in range(15):
        t = []
        for L in board:
            t.append(L[j])
        tt.append(t[-1::-1])
    # 存储副对角线序列
    n = 15
    t1 = []
    for i in range(n + n - 1):
        temp = []
        for j in range(i + 1):
            k = i - j
            if n > k >= 0 and j < n:
                temp.append(board[j][k])
        t1.append(list(temp))
    # 存储主对角线序列
    n = 15
    t2 = []
    for i in range(n + n - 1):
        temp = []
        for j in range(i + 1):
            k = i - j
            if n > k >= 0 and j < n:
                temp.append(tt[j][k])
        t2.append(list(temp))
    # 判断对角线是否形成5子
    for item in t1:
        try:
            if str(item).index('-1, -1, -1, -1, -1'):
                return -1
        except ValueError:
            pass
        try:
            if str(item).index('1, 1, 1, 1, 1'):
                return 1
        except ValueError:
            pass
    for item in t2:
        try:
            if str(item).index('-1, -1, -1, -1, -1'):
                return -1
        except ValueError:
            pass
        try:
            if str(item).index('1, 1, 1, 1, 1'):
                return 1
        except ValueError:
            pass


# 初始化和更新棋盘界面
def draw(screen, board):
    # 画网盘
    for i in range(15):
        start = (space, space + i * size)
        end = (WIDTH - space, space + i * size)
        pygame.draw.line(screen, Black, start, end, 3)
        pygame.draw.line(screen, Black, start[-1::-1], end[-1::-1], 3)
    # 画棋子
    for i in range(15):
        for j in range(15):
            if board[i][j] == BlackPiece:
                point = (space + i * size, space + j * size)
                pygame.draw.circle(screen, Black, point, 19)
            if board[i][j] == WhitePiece:
                point = (space + i * size, space + j * size)
                pygame.draw.circle(screen, white, point, 19)
