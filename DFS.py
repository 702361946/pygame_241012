#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946
#  github.com/702361946/pygame_241012

# 深度优先搜索

import logging
from datetime import datetime

from paths import log_path

if True:
    logging.basicConfig(filename=log_path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'DFS'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# 构造地图
def w_game_map(cells: dict, open_game: int = None, win: int = None)-> dict:
    """
    cells必须为经过w_cell函数构造的cells字典
    必须基于左&上墙同步规则
    将返回一个基于给予cells的字典
    含有cells的邻居关系
    """
    logging.info('w game map')
    if open_game is None:
        open_game = 0

    if win is None:
        for i in range(cells['h'] * cells['w']):
            if cells[i].win is True:
                win = i

    game_map = {
        'win_uid': win,
        'open_uid': open_game,
        'h': cells['h'],
        'w': cells['w']
    }

    # 构造所有点的邻居关系(需要基于左&上墙同步规则开启状态)
    for i in range(cells['h'] * cells['w']):
        game_map[i] = []
        # 北, 东, 南, 西
        # North, East, South, West
        if cells[i].N is False:
            game_map[i].append(i - cells['w'])
        if cells[i].E is False:
            game_map[i].append(i + 1)
        if cells[i].S is False:
            game_map[i].append(i + cells['w'])
        if cells[i].W is False:
            game_map[i].append(i - 1)

    logging.info('game map ok')

    return game_map


# DFS 深度优先搜索
def DFS(game_map: dict, unvisited: list = None, pending: list = None, visited: list = None, dfs_max: int = 50):
    """
    map必须为w_game_map构造的map
    Unvisited未访问列表(默认为开始)
    Pending暂存
    Visited已访问
    """
    logging.info('open DFS')
    # 检查None
    if True:
        if unvisited is None:
            unvisited = []
        if pending is None:
            pending = []
        if visited is None:
            visited = []

    unvisited.append(game_map['open_uid'])
    logging.info(f'win:{game_map['win_uid']}')
    t: int = 0
    while True:
        # 寻找节点
        for i in unvisited:
            if type(i).__name__ == 'int':
                for a in game_map[i]:
                    if not a in pending:
                        pending.append(a)
                if not i in visited:
                    visited.append(i)
            elif type(i).__name__ == 'list':
                for a in i:
                    for b in game_map[a]:
                        if not b in pending:
                            pending.append(b)
                    if not a in visited:
                        visited.append(a)

        # 检查后执行赋值以进行下一步
        if True:
            unvisited = []
            for i in pending:
                if not i in visited:
                    unvisited.append(i)
            # logging.debug(f'u{unvisited}\\v{visited}')
            pending = []

        # 循环判定是否到达了节点
        for i in visited:
            if i == game_map['win_uid']:
                logging.info('DFS is True')
                return True
        else:
            if len(unvisited) == 0 or t >= dfs_max:
                logging.info('DFS is False')
                return False

        t += 1

# DFS(w_game_map(cells))
