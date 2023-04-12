import pygame
import random

class Game:
    def __init__(self):
        # プレイヤーキャラクターの初期化
        self.player_image = pygame.image.load("assets/momotaro.png").convert()
        self.player_image = pygame.transform.scale(self.player_image, (32, 32))
        self.player_pos = [0, 0]
        
        self.akaoni_image = pygame.image.load("assets/akaoni.png").convert()
        self.akaoni_image = pygame.transform.scale(self.akaoni_image, (32, 32))
        self.akaoni_pos = [600, 400]
        self.akaoni_vel = [0, 0]
        self.akaoni_acc = [-0.5, -0.5]  # 加速度

        self.move_amount = 0.1
        self.clock = pygame.time.Clock()

    def update(self):
        # プレイヤーキャラクターの移動
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_pos[0] -= self.move_amount
        if keys[pygame.K_RIGHT]:
            self.player_pos[0] += self.move_amount
        if keys[pygame.K_UP]:
            self.player_pos[1] -= self.move_amount
        if keys[pygame.K_DOWN]:
            self.player_pos[1] += self.move_amount

        # 移動量の調整
        # if self.move_amount > 0.1:
        #     self.move_amount -= 0.01
        # self.clock.tick(60)
        self.akaoni2player_vel = [self.player_pos[0] - self.akaoni_pos[0], self.player_pos[1] - self.akaoni_pos[1]]
        
        # あかおにの移動
        self.akaoni_vel[0] += self.akaoni_acc[0]
        self.akaoni_vel[1] += self.akaoni_acc[1]
        
        max_speed = 5
        self.akaoni_vel[0] = max(min(self.akaoni_vel[0], max_speed), -max_speed)
        self.akaoni_vel[1] = max(min(self.akaoni_vel[1], max_speed), -max_speed)

        
        self.akaoni_pos[0] += self.akaoni_vel[0]
        self.akaoni_pos[1] += self.akaoni_vel[1]

        # 移動量に壁の衝突判定を追加
        if self.akaoni_pos[0] < 0 or self.akaoni_pos[0] > 600:
            self.akaoni_vel[0] = -self.akaoni_vel[0]
        if self.akaoni_pos[1] < 0 or self.akaoni_pos[1] > 400:
            self.akaoni_vel[1] = -self.akaoni_vel[1]
        
    def draw(self, surface):
        # プレイヤーキャラクターの描画
        surface.blit(self.player_image, self.player_pos)
        surface.blit(self.akaoni_image, self.akaoni_pos)