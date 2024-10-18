#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946
#  github.com/702361946/pygame_241012
import logging
from datetime import datetime

import pygame

from paths import log_path, zh_font
from pngs import pngs

if True:
    logging.basicConfig(filename=log_path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'configure_pygame'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 初始化pygame
if True:
    pygame.init()
    pygame.font.init()

    pygame.display.set_caption('走格子')

    game_fps = 60
    pygame.time.Clock().tick(game_fps)

    game_ico = pygame.image.load('pngs\\game.ico')
    pygame.display.set_icon(game_ico)

    colors = {
        '#000000': (0, 0, 0),
        '#ffffff': (255, 255, 255)
    }

    buttons: dict = {}

    fonts = {
        '12': pygame.font.Font(None, 12),
        '24': pygame.font.Font(None, 24),
        '36': pygame.font.Font(None, 36),
        '48': pygame.font.Font(None, 48),
        '60': pygame.font.Font(None, 60),
        'zh-12': pygame.font.Font(zh_font, 12),
        'zh-24': pygame.font.Font(zh_font, 24),
        'zh-36': pygame.font.Font(zh_font, 36),
        'zh-48': pygame.font.Font(zh_font, 48),
        'zh-60': pygame.font.Font(zh_font, 60)
    }

def exit_pygame():
    logging.info('exit pygame')
    pygame.quit()


def down_button(button_name: str,
                x: int,
                y: int,
                w: int,
                h: int,
                color: str,
                com = None,
                button_str = None,
                button_font = None
                ):
    """
    定义一个button
    """
    if button_font is None:
        button_font = fonts['zh-48']
    if button_str is None:
        button_str = 'None'

    buttons[button_name] = {
        'rect': pygame.Rect(x, y, w, h),
        'color': colors[color],
        'def': com,
        'str': button_str,
        'font': button_font
    }
    try:
        if pngs[button_name]:
            buttons[button_name]['png'] = pngs[button_name]

    except KeyError:
        buttons[button_name]['png'] = None

    logging.info(f'{button_name} button ok')


logging.info('pygame ok and exit')
logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
