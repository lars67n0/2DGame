import random
from Data.Constants import WIDTH

Score = 0
player_x = 50
player_y = 510
y_change = 0
x_change = 0
Enemy = [650, 840, 870]
Enemy_Speed = 2
active = False
player_dead = False  # New variable to track player's death
# Variables for falling enemies
falling_enemies = [{'x': random.randint(50, WIDTH - 50), 'y': random.randint(-40, 10)} for _ in range(3)]
falling_speed = 2

class GameVariables:
    def __init__(self):
        self.running = False
        self.active = False
        self.player_x = 0
        self.Enemy = [650, 840, 870]
        self.Score = 0
        self.player_dead = False
        self.x_change = 0
        self.y_change = 0

game_variables = GameVariables()

