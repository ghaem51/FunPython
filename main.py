import sys
import pygame
import threading
import time
import itertools

from back_ground import Floor
from person import Person

width, height = 1680, 860
white = (153, 204, 255)


def check_limits(person, floor):
	if person.x <= 0:
		person.x += person.pace
	if person.x >= floor.width - person.width:
		person.x -= person.pace
	if person.y <= 0:
		person.y += person.pace
	if person.y >= floor.height - person.width:
		person.y -= person.pace

	x, y = person.x + person.width//2, person.y+person.height-20
	for i in range(len(floor.table)):
		for j in range(len(floor.table[i])):
			if floor.table[i][j].content == floor.wall_url:
				wall_rect = pygame.Rect(floor.table[i][j].x, floor.table[i][j].y, 70, 100)
				if wall_rect.collidepoint((x, y)):
					if wall_rect.collidepoint((x-person.pace, y)) == False:
						person.x -= 2*person.pace
					if wall_rect.collidepoint((x+person.pace, y)) == False:
						person.x += 2*person.pace
					if wall_rect.collidepoint((x, y-person.pace)) == False:
						person.y -= 2*person.pace
					if wall_rect.collidepoint((x, y+person.pace)) == False:
						person.y += 2*person.pace


def check_item_on_the_floor(person, floor):
    x, y = person.x + person.width // 2, person.y + person.height - 20
    for i in range(len(floor.table)):
        for j in range(len(floor.table[i])):
            if floor.table[i][j].content in [floor.money_url, floor.laptop_url]:
                obj_rect = pygame.Rect(floor.table[i][j].x, floor.table[i][j].y, 70, 100)
                if obj_rect.collidepoint((x, y)):
					print("collide accured")
                    person.bag.add_to_bag(floor.table[i][j].content)
                    floor.table[i][j].content = ""
                else:
                    if not person.bag.is_bag_empty():
                        obj = person.bag.use_item_in_bag(person.bag.contents[len(person.bag.contents)-1])
                        floor.table[i][j].content = obj


def shake_student(screen, person):
	img_urls = ["./moving_student/" + str(i) + ".png" for i in range(1, 7)]
	for img_url in itertools.cycle(img_urls):
		print(img_url)
		image = pygame.image.load(img_url)
		image = pygame.transform.scale(image, (person.width, person.height))
		screen.blit(image, (person.x, person.y))
		time.sleep(.4)


pygame.init()
sound = pygame.mixer.music.load("./media/walk.mp3")
pygame.mixer.Channel(1).play(pygame.mixer.Sound("./media/bg_music.wav"), loops=-1)
pygame.mixer.Channel(1).set_volume(0.25)

try:
	p = Person(image_url="./media/student_infront.png")
	floor = Floor(wall_url="./media/wall.png")
	running = True
	screen = pygame.display.set_mode((width, height))
	pygame.display.flip()

	while running:
		bg_image = pygame.image.load("./media/bg_image.jpg")
		bg_image = pygame.transform.scale(bg_image, (1680, 860))
		screen.blit(bg_image, (0,0))
		floor.set_walls(screen)
		screen.blit(p.image, (p.x, p.y))

		# floor.draw_table(screen, width, height)

		pygame.display.flip()

		events = pygame.event.get()

		check_limits(p, floor)

		for event in events:
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					p.x -= p.pace
					p.set_image("./media/student_onleft.png")
					pygame.mixer.music.play(-1, 0)
				elif event.key == pygame.K_RIGHT:
					p.x += p.pace
					p.set_image("./media/student_onright.png")
					pygame.mixer.music.play(-1, 0)
				elif event.key == pygame.K_UP:
					p.y -= p.pace
					p.set_image("./media/student_backward.png")
					pygame.mixer.music.play(-1, 0)
				elif event.key == pygame.K_DOWN:
					p.y += p.pace
					p.set_image("./media/student_infront.png")
					pygame.mixer.music.play(-1, 0)
				elif event.key == pygame.K_g:
					check_item_on_the_floor(p, floor)

				if event.type == pygame.KEYUP:
					pygame.mixer.music.stop()
				# gif_thread = threading.Thread(target=shake_student, kwargs={'screen': screen, 'person': p})
				# gif_thread.start()

			check_limits(p, floor)
			pygame.display.update()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			p.x -= p.pace
		elif keys[pygame.K_RIGHT]:
			p.x += p.pace
		elif keys[pygame.K_UP]:
			p.y -= p.pace
		elif keys[pygame.K_DOWN]:
			p.y += p.pace
		pygame.display.update()


	pygame.quit()

finally:
	pygame.quit()
