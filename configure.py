import random
import sys
from collections import defaultdict

import pygame

from jsons import *
from pngs import pngs

if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'configure'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if True:
    game_version = r_json('version')
    if game_version is None:
        logging.error('no version')
        print('未正确配置version')
        input('按下Enter退出')
        exit(1)

# 初始化pygame
if True:
    pygame.init()
    game_fps = 60
    colors = {
        '#000000': (0, 0, 0),
        '#ffffff': (255, 255, 255)
    }
    buttons: dict[pygame.Rect, tuple, pygame.Surface, defaultdict]= {}

    # 以下为窗口实例
    # game_w_h = (w, h)
    # window = pygame.display.set_mode(game_w_h)
    # pygame.display.set_caption('走格子')
    # pygame.time.Clock().tick(game_fps)
    # game_ico = pygame.image.load('pngs\\game.ico')
    # pygame.display.set_icon(game_ico)

    def exit_pygame():
        logging.info('exit pygame')
        pygame.quit()


    def down_button(name: str, x: int, y: int, w: int, h: int, color: str, com: defaultdict = None):
        """
        定义一个button
        """
        buttons[name] = {
            'rect': pygame.Rect(x, y, w, h),
            'color': colors[color],
            'png': pngs[name],
            'def': com
        }
        logging.info(f'{name} button ok')

    logging.info('pygame ok')


def sys_exit(t:int = 0):
    logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    logging.debug(f'sys exit:{t}')
    sys.exit(t)

cells = {}
class Cell:
    """
    设置矩阵格子
    """
    def __init__(self,
                 uid: int,
                 north: bool = random.choice([True,False]),
                 east: bool = random.choice([True,False]),
                 south: bool = random.choice([True,False]),
                 west: bool = random.choice([True, False]),
                 win: bool = False, # 终点判定
                 gain: bool = random.choice([True, False]), # 正增益判定
                 effect: int = random.randint(game_version['effect_min'], game_version['effect_max'])
                 ):
        # 北, 东, 南, 西
        # North, East, South, West
        try:
            self.uid = uid
            self.N = north
            self.E = east
            self.S = south
            self.W = west
            # self.png = pngs[f'{north}{east}{south}{west}'.replace('True', 'T').replace('False', 'F')]
            self.png = None
            self.win = win
            self.gain = gain
            self.effect = effect
            logging.info(f'cell uid:{self.uid}')

        except Exception as e:
            print(e)
            logging.error(e)


def w_cell(h: int,w: int) -> dict:
    """
    h高, w宽, 用以编写字典cells
    """
    # [0,1]
    # [2,3]
    logging.info(f'w cell:{h}*{w}')
    cells['h'] = h
    cells['w'] = w

    t = 0
    win_if = False

    while t < h * w:
        cells[t] = Cell(t)

        # 终点规则
        if not win_if:
            if (random.randint(1, 100) > 90 or t == h * w - 1) and t != 0:
                cells[t].win = True
                win_if = True
                logging.info(f'win cell uid:{t}')

        # 封边规则
        if True:
            if t % w == 0:  # 西
                cells[t].W = True
            if (t + 1) % w == 0:  # 东
                cells[t].E = True
            if t < w:  # 北
                cells[t].N = True
            if t >= h * w - w:  # 南
                cells[t].S = True

        # 其他规则
        if True:
            # 出发点无障碍规则
            if True:
                if w > 1:
                    cells[0].E = False

                if h > 1:
                    cells[0].S = False

            # 终点无障碍规则
            if True:
                if cells[t].win is True:
                    cells[t].W = False
                    cells[t].E = False
                    cells[t].N = False
                    cells[t].S = False
                    if t % w == 0:  # 西
                        cells[t].W = True
                    if (t + 1) % w == 0:  # 东
                        cells[t].E = True
                    if t < w:  # 北
                        cells[t].N = True
                    if t >= h * w - w:  # 南
                        cells[t].S = True

            pass

        t += 1

    logging.info('ok')


logging.info('configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
