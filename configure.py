#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946
#  github.com/702361946/pygame_241012

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

    pygame.display.set_caption('走格子')

    game_fps = 60
    pygame.time.Clock().tick(game_fps)

    game_ico = pygame.image.load('pngs\\game.ico')
    pygame.display.set_icon(game_ico)

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
    北, 东, 南, 西
    North, East, South, West
    """
    def __init__(self,
                 uid: int,
                 north: bool = None,
                 east: bool = None,
                 south: bool = None,
                 west: bool = None,
                 win: bool = False, # 终点判定

                 gain: bool = None, # 正增益判定
                 effect: int = None
                 ):
        # 北, 东, 南, 西
        # North, East, South, West
        try:
            self.uid = uid
            # 墙体
            if True:
                if north is None:
                    self.N = random.choice([True, False])
                else:
                    self.N = north
                if east is None:
                    self.E = random.choice([True, False])
                else:
                    self.E = east
                if south is None:
                    self.S = random.choice([True, False])
                else:
                    self.S = south
                if west is None:
                    self.W = random.choice([True, False])
                else:
                    self.W = west

            # self.png = pngs[f'{north}{east}{south}{west}'.replace('True', 'T').replace('False', 'F')]
            self.png = None
            self.win = win
            # 格子增益效果
            if True:
                if gain is None:
                    self.gain = random.choice([True, False])
                else:
                    self.gain = gain
                if effect is None:
                    self.effect = random.randint(game_version['effect_min'], game_version['effect_max'])
                else:
                    self.effect = effect

            # logging.info(f'cell uid:{self.uid}')

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
            if (random.randint(1, 100) > 90 or t == h * w - 1) and t >= h * w // 2:
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
                try:
                    if w > 1:
                        cells[0].E = False
                        cells[0 + 1].W = False

                    if h > 1:
                        cells[0].S = False
                        cells[0 + w].N = False

                except KeyError:
                    pass

            # 终点无障碍规则
            if True:
                try:
                    if cells[t].win is True:
                        cells[t].W = False
                        cells[t].E = False
                        cells[t].N = False
                        cells[t].S = False
                        if t % w == 0:  # 西
                            cells[t].W = True
                        if (t - 1) % w == 0:  # 东
                            cells[t].E = True
                        if t < w:  # 北
                            cells[t].N = True
                        if t >= h * w - w:  # 南
                            cells[t].S = True

                    # 用来把底下的也改了的
                    # 这堆有bug，貌似还挺大
                    # 检查下一行的Cell是否是终点
                    if (t + w) < (h * w) and cells[t + w].win:
                        cells[t].S = False
                    # 检查下一个Cell是否是终点
                    if (t + 1) < (h * w) and cells[t + 1].win:
                        cells[t].E = False
                    # 检查上一行的Cell是否是终点
                    if t >= w and cells[t - w].win:
                        cells[t].N = False
                    # 检查上一个Cell是否是终点
                    if t % w > 0 and cells[t - 1].win:
                        cells[t].W = False

                except KeyError:
                    pass

            # 左&上墙体同步规则
            if True:
                try:
                    # 左侧墙体同步
                    if not t % w == 0:
                        cells[t - 1].E = cells[t].W
                    # 上侧墙体同步
                    if not t < w:
                        cells[t - w].S = cells[t].N

                except KeyError:
                    pass

            pass

        t += 1

    logging.info('ok')


logging.info('configure ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
