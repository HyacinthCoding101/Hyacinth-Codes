from pygame import *
init()

width = 1600
height = 1000

window = display.set_mode((width, height))
screen = display.get_surface()

playerImg = image.load("spaceship.png")
playerImg = transform.scale(playerImg,(300,80))
player = Rect(650,900,150,80)

invadersImg = image.load("spaceinvaders.png")
invadersImg = transform.scale(invadersImg,(75,25))

invaders = []
bullets = []
y = 0
while y < 4:
	x = 40
	while x <= 1200:
		i = Rect(x,20+(y * 50),50,50)
		invaders.append(i)
		x = x + 150
	y = y + 1

exitProg = False 

# game loop
dx = 2
px = 0 # direction
while exitProg == False:
	# event loop
	for e in event.get():
		if e.type == constants.QUIT:
			exitProg = True 
		if e.type == KEYDOWN:
			if e.key == K_LEFT:
				px = -2
			elif e.key == K_RIGHT:
				px = 2
			elif e.key == K_SPACE:
				nb = Rect(player.x, player.y, 5,10)
				bullets.append(nb)
			if e.type == KEYUP:
				if e.key == K_LEFT or e.key == K_RIGHT:
					px = 0
				
		
	# draw
	screen.fill((0,0,0))
	player.move_ip(px,0)
	screen.blit(playerImg,player)
	for i in invaders:
		if i.colliderect(player):
			exitProg = True
		i.move_ip(dx,0)
	for i in invaders:
		if i.x + 150 > width or i.x < 0:
			dx = dx * -1
			for j in invaders:
				j.move_ip(0,20)
			break
	for i in invaders:
		i.move_ip(dx,0)
	for b in bullets:
		for i in invaders:
			if i.colliderect(b):
				invaders.remove(i)
				bullets.remove(b)
	if len(invaders) == 0:
		exitProg = True
	for b in bullets:
		b.move_ip(0,-5)
	for b in bullets:
		draw.rect(screen, (255,0,0), b)
		
	
	pos = 0
	while pos < len(invaders):
		screen.blit(invadersImg, invaders[pos])
		pos = pos + 1
		
	time.delay(5)
	display.flip()
	
	

