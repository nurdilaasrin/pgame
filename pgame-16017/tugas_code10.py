import pygame

pygame.init()
screen = pygame.display.set_mode((500, 550))
done = False
warna_bg = (30, 100, 59)

pygame.display.set_caption("Hallo APP")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
	event.key == pygame.K_ESCAPE:
			done = True

	screen.fill(warna_bg)
	pygame.draw.line(screen,(22, 198, 12),(300,200,),(300, 300))
	pygame.draw.line(screen,(22, 198, 12),(200,300,),(300, 300))
	pygame.draw.line(screen,(22, 198, 12),(300,200,),(200, 200))
	pygame.draw.line(screen,(22, 198, 12),(200,300,),(200, 200))
	pygame.display.flip()