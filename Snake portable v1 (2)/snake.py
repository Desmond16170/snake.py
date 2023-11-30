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
snake_speed = 15

# Definir la fuente del texto
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(
            game_display, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])


def show_scores():
    scores_file = open("scores.txt", "r")
    scores = scores_file.readlines()
    scores_file.close()

    game_display.fill(white)
    message("Puntuaciones más altas:", black)
    y = height / 2
    for score in scores:
        score_text = score_font.render(score.strip(), True, black)
        game_display.blit(score_text, [width / 3, y])
        y += 40

    pygame.display.update()
    time.sleep(3)


def game_loop():
    game_over = False
    game_close = False

    # Inicializar la posición y la dirección de la serpiente
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    # Inicializar la lista de la serpiente y la longitud de la serpiente
    snake_list = []
    length_of_snake = 1

    # Generar la posición aleatoria de la comida
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Inicializar el reloj del juego
    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            game_display.fill(white)
            message(
                "¡Perdiste! Presiona Q para salir o C para jugar de nuevo",
                red)
            pygame.display.update()

            # Lógica para el menú de inicio
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Lógica para controlar la serpiente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Actualizar la posición de la serpiente
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        game_display.fill(white)
        pygame.draw.rect(
            game_display, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        # Lógica para cuando la serpiente come la comida
        if x1 == foodx and y1 == foody:
            foodx = round(
                random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(
                random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Actualizar la pantalla del juego
        clock.tick(snake_speed)

    # Guardar la puntuación del jugador
    scores_file = open("scores.txt", "a")
    scores_file.write(str(length_of_snake - 1) + "\n")
    scores_file.close()

    # Mostrar las puntuaciones más altas
    show_scores()

    pygame.quit()


# Iniciar el juego
game_loop()
