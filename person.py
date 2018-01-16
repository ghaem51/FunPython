import pygame
from bag import Bag

class Person:
    def __init__(self, image_url):
        self.health = 100
        self.width = 150
        self.x = 50
        self.y = 100
        temp_image = pygame.image.load(image_url)
        self.height = int(temp_image.get_rect().size[1] / temp_image.get_rect().size[0] * self.width)
        self.image = pygame.transform.scale(temp_image, (self.width, self.height))
        self.pace = 30
        self.bag = Bag()

    def set_image(self, img_url):
        img = pygame.image.load(img_url)
        self.image = pygame.transform.scale(img, (self.width, self.height))

    def is_dead(self):
        return self.health <= 0
