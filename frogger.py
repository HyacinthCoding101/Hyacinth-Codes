from pygame import *

init()

width = 1200
height = 800

screen = display.set_mode((width, height))
display.set_caption('Frogger')

frogPic = image.load("frogbg.png")
frogPic = transform.scale(frogPic, (50, 50))
frogRect = Rect(600, 700, 50, 50)

carPic = image.load("car.png")
carPic = transform.scale(carPic, (50, 50))

logPic = image.load("log.png")
logPic = transform.scale(logPic, (50, 50))


cars = []
y = 600 
while y >= 450:  
    x = 1200  
    while x >= 0:  
        carRect = Rect(x, y, 50, 50)
        cars.append(carRect)
        x -= 150  
    y -= 150
    
logs = []
l = 300
while l >= 150:
	x = 1200
	while x >= 0:
		logRect = Rect(x, l, 50, 50)
		logs.append(logRect)
		x -= 150
	l -= 150  

endGame = False
while not endGame:
    for e in event.get():
        if e.type == QUIT:
            endGame = True

        if e.type == KEYUP:
            if e.key == K_w:
                frogRect.move_ip(0, -50)
            if e.key == K_a:
                frogRect.move_ip(-50, 0)
            if e.key == K_d:
                frogRect.move_ip(50, 0)

    screen.fill((0, 0, 0))
    
    # Green field of safety
    draw.rect(screen, (144, 238, 144), (0, 0, width, height))
    
    # Roads of obstacles (black roads)
    draw.rect(screen, (0, 0, 0), (0, 600, width, 100))
    draw.rect(screen, (0, 0, 0), (0, 450, width, 100))
    draw.rect(screen, (0, 101, 255), (0, 300, width, 100))
    draw.rect(screen, (0, 101, 255), (0, 150, width, 100))

    i = 0
    while i < len(cars):
        cars[i].x -= 5  
        if cars[i].x < -50:  
            cars[i].x = width 
        i += 1
        
    b = 0
    while b < len(logs):
        logs[b].x -= 5  
        if logs[b].x < -50:  
            logs[b].x = width 
        b += 1

    screen.blit(frogPic, frogRect)

    i = 0
    while i < len(cars):
        screen.blit(carPic, cars[i])
        i += 1
    
    b = 0
    while b < len(logs):
        screen.blit(logPic, logs[b])
        b += 1

    display.update()
    time.delay(30)

quit()
