import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Platformer Game')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Параметры игрока
player_width = 50
player_height = 60
player_x = 100
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5
player_jump_speed = 10
player_gravity = 0.5

# Состояние игрока
player_velocity_y = 0
player_on_ground = False

# Платформы
platforms = [
    pygame.Rect(100, SCREEN_HEIGHT - 50, 200, 10),
    pygame.Rect(400, SCREEN_HEIGHT - 150, 200, 10),
    pygame.Rect(200, SCREEN_HEIGHT - 250, 200, 10),
]

def draw_player():
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

def move_player():
    global player_x, player_y, player_velocity_y, player_on_ground

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and player_on_ground:
        player_velocity_y = -player_jump_speed
        player_on_ground = False

    player_velocity_y += player_gravity
    player_y += player_velocity_y

    if player_y > SCREEN_HEIGHT - player_height:
        player_y = SCREEN_HEIGHT - player_height
        player_velocity_y = 0
        player_on_ground = True

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_y = platform.top - player_height
            player_velocity_y = 0
            player_on_ground = True

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_player()

        screen.fill(WHITE)
        draw_player()
        draw_platforms()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
