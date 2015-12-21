#coding: utf-8

import pygame


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([1280, 800])

drawables_list = pygame.sprite.Group()


score1 = 0
score2 = 0
done = False





while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				score1 = score1+1
			if event.key == pygame.K_p:
				score2 = score2+1		
			if event.key == pygame.K_a:
				score1 = score1-1
			if event.key == pygame.K_l:
				score2 = score2-1

	if score1<10 and score2<10:
		fsize=900
	elif score1>=10 and score2>=10:
		fsize=600
	else:
		fsize=700
	
	if score1<0:
		score1=0
	if score2<0:
		score2=0
		
	
	screen.fill([255,255,255])		

	scoreTot = str(score1) + " - " + str(score2)
	
	font = pygame.font.Font(None, fsize)
	text = font.render(scoreTot, 1, [0,0,0])
	textpos = text.get_rect()
	textpos.centerx = 1280/2
	textpos.centery = 800/2
	screen.blit(text, textpos)






	drawables_list.draw(screen)

	pygame.display.flip()

	clock.tick(120)

pygame.quit()
