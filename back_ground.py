from block import Block

import pygame

class Floor:
    def __init__(self, wall_url):
        self.width = 1680  # 24 * 70
        self.height = 860  # 20 * 40 + 60
        self.wall_url = wall_url
        self.laptop_url = "./media/laptop.png"
        self.money_url = "./media/money.png"
        self.table = [[Block(i*70, j*40) for j in range(20)] for i in range(24)]

    def draw_table(self, screen, width, height):
        for i in range(21):
            pygame.draw.line(screen, (1, 1, 1), (0, (40)*i), (width, (40)*i))
        for i in range(25):
            pygame.draw.line(screen, (1, 1, 1), (70*i, 0), (70*i, height))

    def set_walls(self, screen):
        img = pygame.image.load(self.wall_url)
        img = pygame.transform.scale(img, (70, 100))
        img_money = pygame.image.load(self.money_url)
        img_money = pygame.transform.scale(img_money, (70, 100))
        img_laptop = pygame.image.load(self.laptop_url)
        img_laptop = pygame.transform.scale(img_laptop, (70, 100))
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if j%6 == 3 and 2 < i < len(self.table) - 3:
                    self.table[i][j].content = self.wall_url
                    screen.blit(img, (i*70, j*40))
                if i == 1 and j == 1:
                    self.table[i][j].content = self.laptop_url
                    screen.blit(img_laptop, (i * 70, j * 40))
                if i == 15 and j == 16:
                    self.table[i][j].content = self.money_url
                    screen.blit(img_money, (i * 70, j * 40))
