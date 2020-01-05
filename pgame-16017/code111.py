# Simpan dengan nama : code111.py
# Pemrograman Game Praktikum 11
# latihan code 11.1 : PyGame
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
warna_bg = (180,100,100)
x,y=0,0
xx,yy=1,1
pygame.display.set_caption("Buat Garis")

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and \
		event.key == pygame.K_ESCAPE:
			done = True
	if event.type == pygame.KEYDOWN and \
		event.key == pygame.K_DOWN:
		yy = yy+1
	if event.type == pygame.KEYDOWN and \
		event.key == pygame.K_UP:
		yy = yy-1
	if event.type == pygame.KEYDOWN and \
		event.key == pygame.K_LEFT:
		xx = xx-1 
	if event.type == pygame.KEYDOWN and \
		event.key == pygame.K_RIGHT:
		xx = xx+1 

	screen.fill(warna_bg)
	pygame.draw.line(screen, (0, 222, 255), (x, y), (xx, yy))
	pygame.display.update()
