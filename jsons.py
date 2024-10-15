#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946
#  github.com/702361946/pygame_241012

import logging
from datetime import datetime

import json
from log_path import path

if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'jsons'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def w_json(a, name: str, language: str = 'utf-8'):
    logging.info(f'w json\\name:{name}\nw:{a}')
    try:
        with open(f'json\\{name}.json', 'w+', encoding=language) as f:
            json.dump(a, f, indent=4, ensure_ascii=False)
            logging.info('ok')

    except Exception as e:
        print(e)
        logging.error(f'\n{e}\n')


def r_json(name: str, language: str = 'utf-8'):
    logging.info(f'r json\\name:{name}')
    try:
        with open(f'json\\{name}.json', 'r+', encoding=language) as f:
            a = json.load(f)
            logging.info(f'ok\nr:{a}')
            return a

    except FileNotFoundError:
        logging.error('未找到文件')
        return None

    except Exception as e:
        print(e)
        logging.error(f'\n{e}\n')
        return None


logging.info('json ok and exit')
logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
