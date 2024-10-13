import pygame

from configure import *
from pngs import pngs

if True:
    logging.basicConfig(filename=path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'game'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 初始化pygame
if True:
    pygame.init()
    game_fps = 60
    colors = {
        '#000000': (0, 0, 0),
        '#ffffff': (255, 255, 255)
    }

    # 以下均为窗口
    # game_w_h = (w, h)
    # window = pygame.display.set_mode(game_w_h)
    # pygame.display.set_caption('走格子')
    # pygame.time.Clock().tick(game_fps)
    # game_ico = pygame.image.load('pngs\\game.ico')
    # pygame.display.set_icon(game_ico)

    def exit_pygame():
        logging.info('exit pygame')
        pygame.quit()

    logging.info('pygame ok')


def open_game():
    pass


def main(h: int, w: int):
    w_cell(h, w)
    game_w_h = (w * 50, h * 50)
    window = pygame.display.set_mode(game_w_h)
    pygame.display.set_caption('走格子')
    pygame.time.Clock().tick(game_fps)
    game_ico = pygame.image.load('pngs\\game.ico')
    pygame.display.set_icon(game_ico)

    def int_if(a: int,f: int) -> bool:
        """
        f:0为上:1为下:2为左:3为右
        """
        if a <= 0 and (f == 0 or f == 2):
            logging.info('false:0')
            return False
        elif a >= (w - 1) * 50 and f == 3:
            logging.info('false:w')
            return False
        elif a >= (h - 1) * 50 and f == 1:
            logging.info('false:h')
            return False
        else:
            logging.info('true:else')
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
                if event.key == pygame.K_w or event.key == pygame.K_UP:
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
                    print('win')

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


if __name__ == '__main__':
    # open_game()
    main(10, 10)
    pass
