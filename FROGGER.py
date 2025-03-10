from pygame import *

# Initialise Pygame
init()

# Set up the display
width = 1200
height = 800
screen = display.set_mode((width, height))
display.set_caption('Frogger')

# Load and scale images
frogPic = image.load("frogbg.png")
frogPic = transform.scale(frogPic, (50, 50))
frogRect = Rect(600, 700, 50, 50)

carPic = image.load("car.png")
carPic = transform.scale(carPic, (50, 50))

otherCarPic = image.load("othercar.png")
otherCarPic = transform.scale(otherCarPic, (50, 50))

logPic = image.load("log.png")
logPic = transform.scale(logPic, (50, 50))

# Create lists for cars and logs

cars = []
y = 600
while y >= 450:
    x = 1200
    while x >= 0:
        carRect = Rect(x, y, 50, 50)
        cars.append(carRect)
        x -= 150
    y -= 150

otherCars = []
o = 550 
while o >= 500:
    x = 0 
    while x <= 1200:
        otherCarRect = Rect(x, o, 50, 50)
        otherCars.append(otherCarRect)
        x += 150
    o -= 50 

logs = []
l = 300
while l >= 150:
    x = 1200
    while x >= 0:
        logRect = Rect(x, l, 50, 50)
        logs.append(logRect)
        x -= 150
    l -= 150

# Game loop
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
    
    # Roads of obstacles
    draw.rect(screen, (0, 0, 0), (0, 600, width, 100))
    draw.rect(screen, (0, 0, 0), (0, 450, width, 200))
    draw.rect(screen, (0, 88, 255), (0, 300, width, 100))
    draw.rect(screen, (0, 88, 255), (0, 150, width, 200))

    # Move cars to the left
    for car in cars:
        car.x -= 2  
        if car.x < -50:  
            car.x = width 
    
    # Move other cars to the right
    for otherCar in otherCars:
        otherCar.x += 5  
        if otherCar.x > width:  
            otherCar.x = -50 

    # Move logs to the left
    for log in logs:
        log.x -= 5  
        if log.x < -50:  
            log.x = width 

    # Draw the frog, cars and logs
    
    screen.blit(frogPic, frogRect)

    for car in cars:
        screen.blit(carPic, car)

    for otherCar in otherCars:
        screen.blit(otherCarPic, otherCar)

    for log in logs:
        screen.blit(logPic, log)

    display.update()
    time.delay(30)

quit()
