import pygame
import time
import random

# Initialisierung des Spiels
pygame.init()

# Fenstergröße und Farben
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Spiel')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 28

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [display_width / 6, display_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            gameDisplay.fill(white)
            message("Du hast verloren! Drücke C zum erneuten Spielen oder Q zum Beenden", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Automatische Steuerung
        if x1 < foodx:
            x1_change = snake_block
            y1_change = 0
        elif x1 > foodx:
            x1_change = -snake_block
            y1_change = 0
        elif y1 < foody:
            y1_change = snake_block
            x1_change = 0
        else:
            y1_change = -snake_block
            x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)

        # Punktzahl anzeigen
        score = Length_of_snake - 1
        score_text = score_font.render("Punkte: " + str(score), True, black)
        gameDisplay.blit(score_text, [10, 10])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()


gameLoop()
