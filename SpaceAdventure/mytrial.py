import pygame
import time
import random
import math
pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Space Adventure")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.png")

# Player
shipImg = pygame.image.load("battleship.png")
shipX = 608 #608
shipY = 600 #600
ship_movementX = 0
ship_movementY = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,1216)
enemyY = random.randint(10,150)
enemy_movementX = 3
enemy_movementY = 10

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 0
bullet_movementY = -10
bullet_fire = False

# Score
score_val = 0
font = pygame.font.Font("freesansbold.ttf", 32)

random_image = pygame.image.load("battleship.png")

def ship(img, x, y):
    screen.blit(img, (x, y))


def bullet(x,y):
    ship(bulletImg, x+16, y-20)


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


def is_collision(en_x, en_y, b_x, b_y):
    en_x += 32
    en_y += 32
    b_x += 16
    b_y += 16
    distance = ((en_x-b_x)**2 + (en_y-b_y)**2)**0.5
    if distance < 27:
        return True
    else:
        return False

def print_score(score_val):
    scoreboard = font.render('Score : '+str(score_val), True, (0, 255, 255))
    screen.blit(scoreboard, (0,0))
# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship(shipImg, shipX, shipY)
    ship(enemyImg, enemyX, enemyY)

    """shipX += movement

    if shipX>=1216 or shipX<=0:
        movement = -1 * movement
"""

    """i =0
    k=1
    while i >=0:
        if i==1216:
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
                ship_movementX = -6
            if event.key == pygame.K_RIGHT:
                ship_movementX = 6
            if event.key == pygame.K_UP:
                ship_movementY = -6
            if event.key == pygame.K_DOWN:
                ship_movementY = 6
            if event.key == pygame.K_p:
                stop_ship()
            if event.key == pygame.K_c:
                stop_ship()
                centre_ship()
            if event.key == pygame.K_SPACE:
                if not bullet_fire:
                    bullet_fire = True
                    bulletX = shipX
                    bulletY = shipY

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
    if shipX < 0:
        shipX = 0
    elif shipX > 1216:
        shipX = 1216
    if shipY <= 50: #50
        shipY = 50  #50
    elif shipY > 700:
        shipY = 700

    enemyX += enemy_movementX
    if not 0 <= enemyX <= 1216:
        enemy_movementX *= -1
        enemyY += enemy_movementY

    if bullet_fire:
        bullet(bulletX, bulletY)
        bulletY += bullet_movementY
    if bulletY < 0:
        bullet_fire = False

    if is_collision(enemyX, enemyY, bulletX, bulletY):
        score_val += 1
        print(score_val)
        bulletY = enemyY
        bullet_fire = False

    print_score(score_val)

    screen.blit (random_image , (1216,700))
    pygame.display.update()
