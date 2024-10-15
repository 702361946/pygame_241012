#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946
#  github.com/702361946/pygame_241012

import logging
import os
from datetime import datetime

import pygame

from jsons import r_json
from log_path import path

if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'pngs'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

pygame.init()

try:
    pngs = {}
    for dirpath, dirnames, filenames in os.walk('pngs'):
        for filename in filenames:
            # 检查文件是否以.png结尾
            if filename.lower().endswith('.png'):
                # xxx.png
                pngs[filename.split('.')[0]] = pygame.image.load(f'pngs\\{filename}')

    for i in r_json('pngs'):
        if pngs[i]:
            pass

except KeyError as e:
    logging.error(f'key:{e}')
    input('Critical files are missing, cannot continue operation.')
    exit(1)

except Exception as e:
    logging.error(e)
    print(e)
    input('')
    exit(1)


logging.info('pngs ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
