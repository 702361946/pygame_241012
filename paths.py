#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946
#  github.com/702361946/pygame_241012

import logging
import os
from datetime import datetime

# 获取当前用户的AppData路径
log_path = os.path.expanduser('~\\AppData')
# windows字体库路径
# font_path = 'C:\\Windows\\Fonts'
zh_font = 'C:\\Windows\\Fonts\\simfang.ttf'

# 检查操作系统，Windows，拼接LocalLow路径
if os.name == 'nt':
    log_path = os.path.join(log_path, 'LocalLow\\702361946\\走格子\\game.log')
else:
    # 对于其他系统，可能没有LocalLow，自定义路径
    log_path = '.\\game.log'  # 请根据实际情况修改

# 目录补全
os.makedirs(os.path.dirname(log_path), exist_ok=True)

if True:
    logging.basicConfig(filename=log_path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'log_path'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info(log_path)

logging.info('log_path ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
