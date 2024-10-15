#  Copyright (c) 2024.
#  702361946@qq.com
#  github.com/702361946
#  github.com/702361946/pygame_241012

from DFS import *
from configure import *

if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'game'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 以下为pygame窗口实例
"""
game_w_h = (w, h)
window = pygame.display.set_mode(game_w_h)
pygame.display.set_caption('走格子')
pygame.time.Clock().tick(game_fps)
game_ico = pygame.image.load('pngs\\game.ico')
pygame.display.set_icon(game_ico)
"""


# 开始游戏
def open_game():
    game_w_h = (100, 200)
    window = pygame.display.set_mode(game_w_h)

    # 用到的button
    if True:
        # 随机模式
        # specify为True的时候为指定模式
        if game_version['random_specify']:
            down_button('random_game',
                        0,
                        0,
                        100,
                        50,
                        '#ffffff',
                        lambda: random_game(game_version['random_h'], game_version['random_w'])
            )

        else:
            down_button('random_game',
                        0,
                        0,
                        100,
                        50,
                        '#ffffff',
                        lambda: random_game(
                            random.randint(game_version['random_min'], game_version['random_max']),
                            random.randint(game_version['random_min'], game_version['random_max'])
                        )
            )

        # 关卡模式
        down_button('lv_game',
                    0,
                    50,
                    100,
                    50,
                    '#ffffff',
                    lambda: lv_game(game_version['lv'])
        )

        # 游戏设置
        down_button('game_settings',
                    0,
                    100,
                    100,
                    50,
                    '#ffffff',
        )

        # 退出游戏
        down_button('exit_game',
                    0,
                    150,
                    100,
                    50,
                    '#ffffff',
                    lambda: sys_exit()
        )

        # 游戏胜利界面确认button
        down_button('ok',
                    50,
                    100,
                    100,
                    50,
                    '#ffffff',
        )


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info('quit game')
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in buttons.keys():
                    if buttons[i]['rect'].collidepoint(event.pos):
                        logging.info(f'down button {i}')
                        if not buttons[i]['def'] is None:
                            buttons[i]['def']()

        window.fill(colors['#ffffff'])

        # 随机模式button
        if True:
            pygame.draw.rect(window, buttons['random_game']['color'], buttons['random_game']['rect'])
            window.blit(buttons['random_game']['png'], (0, 0))

        # 关卡模式button
        if True:
            pygame.draw.rect(window, buttons['lv_game']['color'], buttons['lv_game']['rect'])
            window.blit(buttons['lv_game']['png'], (0, 50))

        # 游戏设置button
        if True:
            pygame.draw.rect(window, buttons['game_settings']['color'], buttons['game_settings']['rect'])
            window.blit(buttons['game_settings']['png'], (0, 100))

        # 退出游戏button
        if True:
            pygame.draw.rect(window, buttons['exit_game']['color'], buttons['exit_game']['rect'])
            window.blit(buttons['exit_game']['png'], (0, 150))

        pygame.display.flip()


# 随机游戏
def random_game(h: int, w: int):
    while True:
        w_cell(h, w)
        if not game_version['random_DFS'] or DFS(w_game_map(cells)):
            break

    game_w_h = (w * 50, h * 50)
    window = pygame.display.set_mode(game_w_h)

    def int_if(a: int,f: int) -> bool:
        """
        f:0为上:1为下:2为左:3为右
        """
        if a <= 0 and (f == 0 or f == 2):
            return False
        elif a >= (w - 1) * 50 and f == 3:
            return False
        elif a >= (h - 1) * 50 and f == 1:
            return False
        else:
            return True

    running = True
    my_xy: [int, int] = [0, 0]
    my_cell: int = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys_exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    logging.info('exit random game')
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if int_if(my_xy[1], 0) and not cells[my_cell].N and not cells[my_cell - w].S:
                        my_xy[1] -= 50
                        my_cell -= w
                        logging.info('up:true')
                    else:
                        logging.info('up:false')
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if int_if(my_xy[1], 1) and not cells[my_cell].S and not cells[my_cell + w].N:
                        my_xy[1] += 50
                        my_cell += w
                        logging.info('down:true')
                    else:
                        logging.info('down:false')
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if int_if(my_xy[0], 2) and not cells[my_cell].W and not cells[my_cell - 1].E:
                        my_xy[0] -= 50
                        my_cell -= 1
                        logging.info('left:true')
                    else:
                        logging.info('left:false')
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if int_if(my_xy[0], 3) and not cells[my_cell].E and not cells[my_cell + 1].W:
                        my_xy[0] += 50
                        my_cell += 1
                        logging.info('right:true')
                    else:
                        logging.info('right:false')

                # 获胜判定
                if cells[my_cell].win is True:
                    logging.info('win')
                    running = False
                    game_win()

        window.fill(colors['#ffffff'])
        for t in range(h * w):
            cells[t].png = pngs[f'{cells[t].N}{cells[t].E}{cells[t].S}{cells[t].W}'.replace('True', 'T').replace('False', 'F')]
            if cells[t].png:  # 如果 Cell 有图片，则绘制
                x = t % w * 50  # 计算 x 坐标
                y = t // w * 50  # 计算 y 坐标
                window.blit(cells[t].png, (x, y))  # 绘制图片

            if cells[t].win is True:
                x = t % w * 50  # 计算 x 坐标
                y = t // w * 50  # 计算 y 坐标
                window.blit(pngs['win'], (x, y))

        window.blit(pngs['my'], (my_xy[0], my_xy[1]))

        pygame.display.flip()  # 更新屏幕显示


# 关卡模式
def lv_game(lv: int = None):
    if lv is None:
        lv = 0

    lvs = r_json('lvs')[f'{lv}']
    for i in range(lvs['w'] * lvs['h']):
        cells[i] = Cell(
            i,
            north = lvs[f'{i}'][0],
            east = lvs[f'{i}'][1],
            south = lvs[f'{i}'][2],
            west = lvs[f'{i}'][3],
            win = lvs[f'{i}'][4]
        )
    logging.info(f'lv:{lv}')


    w = lvs['w']
    h = lvs['h']
    game_w_h = (w * 50, h * 50)
    window = pygame.display.set_mode(game_w_h)

    def int_if(a: int, f: int) -> bool:
        """
        f:0为上:1为下:2为左:3为右
        """
        if a <= 0 and (f == 0 or f == 2):
            return False
        elif a >= (w - 1) * 50 and f == 3:
            return False
        elif a >= (h - 1) * 50 and f == 1:
            return False
        else:
            return True

    running = True
    my_xy: [int, int] = [0, 0]
    my_cell: int = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys_exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    logging.info('exit lv game')
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if int_if(my_xy[1], 0) and not cells[my_cell].N and not cells[my_cell - w].S:
                        my_xy[1] -= 50
                        my_cell -= w
                        logging.info('up:true')
                    else:
                        logging.info('up:false')
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if int_if(my_xy[1], 1) and not cells[my_cell].S and not cells[my_cell + w].N:
                        my_xy[1] += 50
                        my_cell += w
                        logging.info('down:true')
                    else:
                        logging.info('down:false')
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if int_if(my_xy[0], 2) and not cells[my_cell].W and not cells[my_cell - 1].E:
                        my_xy[0] -= 50
                        my_cell -= 1
                        logging.info('left:true')
                    else:
                        logging.info('left:false')
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if int_if(my_xy[0], 3) and not cells[my_cell].E and not cells[my_cell + 1].W:
                        my_xy[0] += 50
                        my_cell += 1
                        logging.info('right:true')
                    else:
                        logging.info('right:false')

                # 获胜判定
                if cells[my_cell].win is True:
                    logging.info('win')
                    running = False
                    game_win()

        window.fill(colors['#ffffff'])
        for t in range(h * w):
            cells[t].png = pngs[
                f'{cells[t].N}{cells[t].E}{cells[t].S}{cells[t].W}'.replace('True', 'T').replace('False', 'F')]
            if cells[t].png:  # 如果 Cell 有图片，则绘制
                x = t % w * 50  # 计算 x 坐标
                y = t // w * 50  # 计算 y 坐标
                window.blit(cells[t].png, (x, y))  # 绘制图片

            if cells[t].win is True:
                x = t % w * 50  # 计算 x 坐标
                y = t // w * 50  # 计算 y 坐标
                window.blit(pngs['win'], (x, y))

        window.blit(pngs['my'], (my_xy[0], my_xy[1]))

        pygame.display.flip()  # 更新屏幕显示


# 游戏胜利
def game_win():
    game_w_h = (200, 150)
    window = pygame.display.set_mode(game_w_h)


    t_if = True
    while t_if:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info('quit game')
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons['ok']['rect'].collidepoint(event.pos):
                    logging.info(f'down button ok')
                    t_if = False


        window.fill(colors['#ffffff'])

        # 获胜图片
        window.blit(pngs['game_win'], (0, 0))

        # 确定button
        if True:
            pygame.draw.rect(window, buttons['ok']['color'], buttons['ok']['rect'])
            window.blit(buttons['ok']['png'], (50, 100))

        pygame.display.flip()


if __name__ == '__main__':
    open_game()
    pass
