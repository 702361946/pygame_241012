#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946
#  github.com/702361946/pygame_241012

import logging
import os
from datetime import datetime

# 获取当前用户的AppData路径
appdata_path = os.path.expanduser('~\\AppData')

# 检查操作系统，Windows，拼接LocalLow路径
if os.name == 'nt':
    path = os.path.join(appdata_path, 'LocalLow\\702361946\\走格子\\game.log')
else:
    # 对于其他系统，可能没有LocalLow，自定义路径
    path = '.\\game.log'  # 请根据实际情况修改

# 目录补全
os.makedirs(os.path.dirname(path), exist_ok=True)

if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'path'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info(path)

logging.info('path ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
