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
carRect = Rect(1150, 650, 50, 50)


endGame = False
while endGame == False:
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
    
    # green field of safety
    draw.rect(screen, (144, 238, 144), (0, 0, width, height))
    
    # roads of obstacles
    draw.rect(screen, (0, 0, 0), (0, 600, width, 100))
    draw.rect(screen, (0, 0, 0), (0, 450, width, 100))
    draw.rect(screen, (0, 0, 0), (0, 300, width, 100))
    draw.rect(screen, (0, 0, 0), (0, 150, width, 100))
   
    
    
    
    screen.blit(frogPic, frogRect)
    screen.blit(carPic, carRect)
    display.update()
    time.delay(30)


quit()
