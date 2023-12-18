import pygame
import random
from Data.Constants import *
from Data.Text import DeathMessage, PauseMessage
from Data.Variables import *
from Player.Methods import check_collision

# initialize Pygame
pygame.init()

# Load player images
player_images = [pygame.image.load(f'PlayerAni/Player{i}.png') for i in range(1, 7)]
current_player_image = 0  # Index of the current player image



# Creating Game Window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Space Runner')
background_image = pygame.image.load('Background/BackgroundTest1.png')
background_x = 0

# Load Background Music
pygame.mixer.music.load('GameMusic.mp3')
pygame.mixer.music.play(-1)

# Load enemy image
enemy_image = pygame.image.load('EnemyAni/enemy.png')

fps = 60
font = pygame.font.Font('freesansbold.ttf', 32)
timer = pygame.time.Clock()

# Function to check collision

running = True

while running:
    timer.tick(fps)
    background_x -= 1
    if background_x < -background_image.get_width():
        background_x = 0

    
    # Order Of Layers
    # Screen Background
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_image.get_width(), 0))

    # Score text
    Score_text = font.render(f'Score: {Score}', True, white)
    screen.blit(Score_text, (580, 80))

    
    # Floor Location and Color
    floor = pygame.draw.rect(screen, cyan, [0, 545, WIDTH, 60]), pygame.draw.rect(screen, darkCyan, [0, 550, WIDTH, 60])

    # Ceiling
    ceiling = pygame.draw.rect(screen, cyan, [0, 6, WIDTH, 60]), pygame.draw.rect(screen, darkCyan, [0, 1, WIDTH, 60])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Game Not Running
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                active = True
                player_x = 50
                Enemy = [650, 840, 870]
                Score = 0
                player_dead = False  # Reset player_dead when starting a new game

        # Game Running
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 22
            if event.key == pygame.K_d:
                x_change = 5
            if event.key == pygame.K_a:
                x_change = -5
            if event.key == pygame.K_ESCAPE:
                active = not active

        # If Player Stops Pressing A/D Stop Moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                x_change = 0
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_ESCAPE:
                active == False

    for i in range(len(Enemy)):
        if active and not player_dead:  # Check if the player is active and not dead
            Enemy[i] -= Enemy_Speed + Score // 100
            background_x = background_x + 10 // 500
            if Enemy[i] < -20:
                Enemy[i] = random.randint(820, 930)
                Score += 10

            # Draw enemy
            screen.blit(enemy_image, (Enemy[i], 510))

            # Check collision
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            enemy_rect = pygame.Rect(Enemy[i], 510, 40, 40)
            if check_collision(player_rect, enemy_rect):
                active = False
                player_dead = True  # Player is dead
                player_x = 50
                player_y = 510
                y_change = 0
                x_change = 0
                falling_enemies = [{'x': random.randint(50, WIDTH - 50), 'y': random.randint(-40, -10)} for _ in range(3)]
                Score = 0

    if active == False:
        pause_text = font.render(PauseMessage, True, white)
        screen.blit(pause_text, (WIDTH // 2 - 320, HEIGHT // 2 - 20))

    if player_dead:
        # Display death message
        death_text = font.render(DeathMessage, True, white)
        screen.blit(death_text, (WIDTH // 2 - 320, HEIGHT // 2 - 50))

    # X Movement
    if 0 <= player_x <= 760:
        player_x += x_change

    # Boundary Condition
    if player_x < 0:
        player_x = 0
    if player_x > 760:
        player_x = 760

    # Jump Y Logic and Movement
    if y_change > 0 or player_y < 510:
        player_y -= y_change
        y_change -= gravity

    # Check ur Location
    if player_y > 510:
        player_y = 510

    # Allows U to jump again
    if player_y == 510 and y_change < 0:
        y_change = 0
    if active and not player_dead:
        for enemy in falling_enemies:
            enemy['y'] += falling_speed + Score // 100
            if enemy['y'] > HEIGHT:
                enemy['x'] = random.randint(50, WIDTH - 50)
                enemy['y'] = random.randint(-40, -10)
                Score += 10

            # Draw falling enemy
            screen.blit(enemy_image, (enemy['x'], enemy['y']))

    # Check collision
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 40, 40)
            if check_collision(player_rect, enemy_rect):
                    active = False
                    player_dead = True  # Player is dead
                    # Reset game variables when player dies
                    player_x = 50
                    player_y = 510
                    y_change = 0
                    x_change = 0
                    falling_enemies = [{'x': random.randint(50, WIDTH - 50), 'y': random.randint(-40, -10)} for _ in range(3)]
                    Score = 0
    # Draw player
    screen.blit(player_images[current_player_image], (player_x, player_y))
    current_player_image = (current_player_image + 1) % len(player_images)


    pygame.display.flip()

pygame.quit()
