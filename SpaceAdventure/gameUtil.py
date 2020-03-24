"""Contains different classes for in-game objects"""
import pygame
import random
import math
pygame.init()
background_img = pygame.image.load("background.png")
font = pygame.font.Font("Rogue_Hero_Expanded_Italic.ttf", 32)


# General Game Functionalities
def background(screen):
    screen.blit(background_img, (0, 0))


def show_enemies(screen, enemies):
    for enemy in enemies:
        enemy.show_enemy(screen)


def key_down_movement(event, player1):
    if event.key == pygame.K_LEFT:
        player1.go_left()
    if event.key == pygame.K_RIGHT:
        player1.go_right()
    if event.key == pygame.K_UP:
        player1.go_up()
    if event.key == pygame.K_DOWN:
        player1.go_down()


def key_up_movement(event, player1):
    if event.key == pygame.K_LEFT:
        player1.go_right()
        # print('left key up')
    if event.key == pygame.K_RIGHT:
        player1.go_left()
        # print('right key up')
    if event.key == pygame.K_UP:
        player1.go_down()
        # print('upward key up')
    if event.key == pygame.K_DOWN:
        player1.go_up()
        # print('downward key up')


def show_bullets(screen, bullets):
    i = 0
    while i < len(bullets):
        bullet = bullets[i]
        if bullet.is_onscreen():
            bullet.show_bullet(screen)
            i += 1
        else:
            bullets.pop(i)
            del bullet


def check_collisions(screen, bullets, enemies, player):
    i = 0
    while i < len(enemies):
        j = 0
        while j < len(bullets):
            if is_colliding(screen, enemies[i], bullets[j]):
                enemies[i] = Enemy()
                player.increase_score()
                del bullets[j]
                break
            j += 1
        else:
            i += 1


def is_colliding(screen, bullet, enemy):
    b_x, b_y = bullet.get_pos()
    e_x, e_y = enemy.get_pos()

    b_x += 16
    b_y += 16
    e_x += 32
    e_y += 32

    distance = math.sqrt((b_x-e_x)**2 + (b_y-e_y)**2)

    if distance < 63:
        explosion(screen,enemy)
        return True
    else:
        return False


def scoreboard(screen, player):
    score = font.render('Score : ' + str(player.get_score()), True, (0, 255, 255))
    screen.blit(score, (0, 0))
    name = font.render('ALANKRIT', True, (0, 255, 255))
    screen.blit(name, (1000, 0))


def laser_sound():
    sound = pygame.mixer.Sound("laser.wav")
    sound.play()


def explosion(screen, enemy):
    sound = pygame.mixer.Sound("explosion.wav")
    sound.play()
    img = pygame.image.load("explosion.png")
    screen.blit(img, enemy.get_pos())
    pygame.display.update()


# Vehicle Functionalities
class Player:
    def __init__(self):
        self.__player_img = pygame.image.load("battleship.png")
        self.__player_x = 608
        self.__player_y = 600
        self.__change_x = 0
        self.__change_y = 0
        self.__score = 0

    def increase_score(self):
        self.__score += 1

    def show_player(self, screen):
        screen.blit(self.__player_img, self.get_pos())

    # Movement Control Functions
    def go_left(self):
        self.__change_x -= 6

    def go_right(self):
        self.__change_x += 6

    def go_up(self):
        self.__change_y -= 6

    def go_down(self):
        self.__change_y += 6

    def stop_player(self):
        self.__change_x = 0
        self.__change_y = 0

    def __move_player(self):
        self.__player_x += self.__change_x
        self.__player_y += self.__change_y

        if self.__player_x < 0:
            self.__player_x = 0
        elif self.__player_x > 1216:
            self.__player_x = 1216

        if self.__player_y < 50:
            self.__player_y = 50
        elif self.__player_y > 656:
            self.__player_y = 656

    # Getters
    def get_pos(self):
        self.__move_player()
        return self.__player_x, self.__player_y

    def get_score(self):
        return self.__score


class Enemy:
    def __init__(self):
        self.__enemy_img = pygame.image.load("enemy.png")
        self.__enemy_x = random.randint(0, 1216)
        self.__enemy_y = random.randint(10, 150)
        self.__change_x = 3

    def show_enemy(self, screen):
        self.__move_enemy()
        screen.blit(self.__enemy_img, (self.__enemy_x, self.__enemy_y))

    def __move_enemy(self):
        self.__enemy_x += self.__change_x
        self.__enemy_y += 0.3
        if not (0 <= self.__enemy_x <= 1216):
            self.__change_x *= -1
        #     self.__enemy_y += 10

    def get_pos(self):
        return self.__enemy_x, self.__enemy_y


class Bullet:
    def __init__(self, player):
        self.__image = pygame.image.load("bullet.png")
        self.__bullet_x, self.__bullet_y = player.get_pos()
        self.__bullet_x += 16
        self.__bullet_y -= 16

    def show_bullet(self, screen):
        self.__move_bullet()
        screen.blit(self.__image, (self.__bullet_x, self.__bullet_y))

    def __move_bullet(self):
        self.__bullet_y -= 10

    def get_pos(self):
        return self.__bullet_x, self.__bullet_y

    def is_onscreen(self):
        if self.__bullet_y > 5:
            return True
