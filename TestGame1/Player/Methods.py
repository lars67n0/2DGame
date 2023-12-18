import pygame
import random
from Data.Variables import *
from Data.Constants import *

def check_collision(player_rect, enemy_rect):
    return player_rect.colliderect(enemy_rect)


def handle_event(event):
    global running, active, player_x, Enemy, Score, player_dead, x_change, y_change

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
            active = False