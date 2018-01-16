import threading
import time
import pygame

class GifThread(threading.Thread):
    def __init__(self, screen, person):
        threading.Thread.__init__(self)

    def run(self):
        img_urls = ["./moving_student/"+str(i)+".png" for i in range(1, 7)]
        for img_url in img_urls:
            image = pygame.image.load(img_url)
            image = pygame.transform.scale(image, (100, 130))
            screen.blit(image, (person.x, person.y))
            time.sleep(.5)


