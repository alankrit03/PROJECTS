import pygame
import gameUtil

pygame.init()
screen = pygame.display.set_mode((1280, 720))


def basic_setup():
    pygame.display.set_caption("Space Adventure")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
    pygame.mixer.music.load("new_background.wav")
    pygame.mixer.music.play(-1)


basic_setup()
player1 = gameUtil.Player()
enemies = [gameUtil.Enemy() for _ in range(10)]
bullets = []
running = True

# Main Game Loop
while running:
    gameUtil.background(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keystroke checking mechanism
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameUtil.laser_sound()
                bullets.append(gameUtil.Bullet(player1))
            else:
                gameUtil.key_down_movement(event, player1)

        if event.type == pygame.KEYUP:
            gameUtil.key_up_movement(event, player1)

    player1.show_player(screen)
    gameUtil.show_enemies(screen, enemies)
    gameUtil.show_bullets(screen, bullets)
    gameUtil.check_collisions(screen, bullets, enemies, player1)
    gameUtil.scoreboard(screen, player1)
    pygame.display.update()

pygame.quit()
