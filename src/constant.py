# 窗口大小
WIDTH, HEIGHT = 660, 660
# 棋盘大小
ROW, COLUMN = 15, 15
# 上下左右的空格
space = 50
# 棋盘格边长
size = 40
# 初始化棋盘,0表示空白，1表示落黑子，-1表示落白子
board = [[0] * 15 for i in range(15)]
BlackPiece, WhitePiece = 1, -1
# 模式,1表示单人模式，2表示多人模式
MODE = 1
# 游戏名称
GameTitle = '五子棋'
# 棋盘背景颜色
SandyBrown = (244, 164, 96)
BurlyWood = (255, 211, 155)
Wheat = (139, 126, 102)
# 线条颜色
Black = (0, 0, 0)
white = (255, 255, 255)
# 棋盘坐标映射
position_map = {
    range(30, 70): 0,
    range(70, 110): 1,
    range(110, 150): 2,
    range(150, 190): 3,
    range(190, 230): 4,
    range(230, 270): 5,
    range(270, 310): 6,
    range(310, 350): 7,
    range(350, 390): 8,
    range(390, 430): 9,
    range(430, 470): 10,
    range(470, 510): 11,
    range(510, 550): 12,
    range(550, 590): 13,
    range(590, 630): 14
}
