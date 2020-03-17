import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1024, 720))

pygame.display.set_caption("Space Adventure")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player
shipImg = pygame.image.load("battleship.png")
shipX = 480
shipY = 600
# shipX = 0
ship_movementX = 0
ship_movementY = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = 0
enemyY = 100
enemy_movementX = 1


def ship(img, x, y):
    screen.blit(img, (x, y))


def centre_ship():
    global shipX
    global shipY
    shipY = 600
    shipX = 480


def stop_ship():
    global ship_movementX
    global ship_movementY
    ship_movementY = 0
    ship_movementX = 0


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    ship(shipImg, shipX, shipY)

    """shipX += movement

    if shipX>=960 or shipX<=0:
        movement = -1 * movement
"""

    """i =0
    k=1
    while i >=0:
        if i==960:
            k = -1
        screen.fill((0, 0, 0))
        ship(i, shipY)
        # pygame.time.delay(1)
        pygame.display.update()
        i +=k"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke checking mechanism
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_movementX = -1
            if event.key == pygame.K_RIGHT:
                ship_movementX = 1
            if event.key == pygame.K_UP:
                ship_movementY = -1
            if event.key == pygame.K_DOWN:
                ship_movementY = 1
            if event.key == pygame.K_p:
                stop_ship()
            if event.key == pygame.K_c:
                stop_ship()
                centre_ship()

        if event.type == pygame.KEYUP:
            stop_ship()

    """for i in range(256):
        screen.fill((1,i,i))
        player()
        pygame.time.delay(5)
        pygame.display.update()
    for i in range(255,-1,-1):
        screen.fill((1,i,i))
        player()
        pygame.time.delay(5)
        pygame.display.update()
"""

    shipX += ship_movementX
    shipY += ship_movementY

    if not 0 <= shipX <= 960:
        ship_movementX = 0
    if not 0 <= shipY <= 654:
        ship_movementY = 0

    ship(enemyImg, enemyX, enemyY)
    enemyX += enemy_movementX
    if not 0 <= enemyX <= 960:
        enemy_movementX *= -1
    pygame.display.update()
