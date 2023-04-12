import pygame
from game import Game
import sys

# Pygameの初期化
pygame.init()

# ゲームウィンドウの設定
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

# ゲームオブジェクトの作成
game = Game()

# # 赤い四角形を描画
# rect1 = pygame.Rect(100, 100, 200, 200)
# pygame.draw.rect(WIN, (255, 0, 0), rect1)

# # 青い四角形を描画
# rect2 = pygame.Rect(300, 100, 200, 200)
# pygame.draw.rect(WIN, (0, 0, 255), rect2)

# ゲームループ
while True:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # rect1.x += 1
    # pygame.display.update(rect1)
    # rect2.y += 1
    # pygame.display.update(rect2)

    # ゲームの更新
    game.update()

    # ゲームの描画
    #WIN.fill((255, 255, 255))  # ゲームウィンドウの背景色を白に設定
    game.draw(WIN)

    # 画面の更新
    pygame.display.update()