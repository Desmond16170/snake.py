import pygame
import time
import random

# Inicializar el juego
pygame.init()

# Definir los colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Definir el tamaño de la pantalla
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Definir la velocidad del juego y el tamaño de la serpiente
snake_block = 10
snake_speed = 20

# Definir la fuente del texto
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Lógica de juego
def game_loop():
    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0
    snake_list = []
    length_of_snake = 1
    foodx, foody = get_random_position()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                handle_keydown(event, x1_change, y1_change)

        x1, y1, x1_change, y1_change = update_snake_position(x1, y1, x1_change, y1_change)
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block, snake_block])
        snake_list, length_of_snake = update_snake_list(snake_list, length_of_snake, x1, y1)
        check_collision(x1, y1, snake_list)

        our_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = get_random_position()
            length_of_snake += 1

        clock.tick(snake_speed)

# Funciones auxiliares
def get_random_position():
    return round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0

def handle_keydown(event, x1_change, y1_change):
    if event.key == pygame.K_LEFT and x1_change == 0:
        x1_change = -snake_block
        y1_change = 0
    elif event.key == pygame.K_RIGHT and x1_change == 0:
        x1_change = snake_block
        y1_change = 0
    elif event.key == pygame.K_UP and y1_change == 0:
        y1_change = -snake_block
        x1_change = 0
    elif event.key == pygame.K_DOWN and y1_change == 0:
        y1_change = snake_block
        x1_change = 0

def update_snake_position(x1, y1, x1_change, y1_change):
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        pygame.quit()
        quit()
    x1 += x1_change
    y1 += y1_change
    return x1, y1, x1_change, y1_change

def update_snake_list(snake_list, length_of_snake, x1, y1):
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]
    return snake_list, length_of_snake

def check_collision(x1, y1, snake_list):
    for x in snake_list[:-1]:
        if x == [x1, y1]:
            pygame.quit()
            quit()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], snake_block, snake_block])

# Iniciar el juego
game_loop()
