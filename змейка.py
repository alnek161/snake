import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 150, 102)
#цвет первой змейки
black = (0, 0, 0)
#цвет второй змейки
black2 = (140, 255, 255)
red = (213, 50, 80)
#яблоки
green = (213, 50, 80)
#фон
blue = (30, 100, 40)

dis_width = 1000
dis_height = 800

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Pythonist')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 50

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def Your_score2(score):
    value = score_font.render("Your Score: " + str(score), True, black2)
    dis.blit(value, [750, 0])

def Winner(score1, score2):
    if score1 == 0:
        value = score_font.render("Учи уроки, дебил", True, yellow)
        dis.blit(value, [300, 300])
    elif score1 > score2:
        value = score_font.render("Black win", True, black)
        dis.blit(value, [300, 300])
    elif score1 == score2:
        value = score_font.render("Draw", True, yellow)
        dis.blit(value, [300, 300])
    else:
        value = score_font.render("Blue win", True, black2)
        dis.blit(value, [300, 300])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def our_snake2(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black2, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x2 = dis_width / 2
    y2 = dis_height / 2

    x1_change = 0
    y1_change = 0
    x2_change = 0
    y2_change = 0

    snake_List = []
    snake_List2 = []
    Length_of_snake = 1
    Length_of_snake2 = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        value = random.randint(0, 50)
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            Your_score2(Length_of_snake2 - 1)
            if value == 10:
                Length_of_snake = 0
            Winner(Length_of_snake, Length_of_snake2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0
                if event.key == pygame.K_LEFT and x2_change != snake_block:
                    x2_change = -snake_block
                    y2_change = 0
                elif event.key == pygame.K_RIGHT and x2_change != -snake_block:
                    x2_change = snake_block
                    y2_change = 0
                elif event.key == pygame.K_UP and y2_change != snake_block:
                    y2_change = -snake_block
                    x2_change = 0
                elif event.key == pygame.K_DOWN and y2_change != -snake_block:
                    y2_change = snake_block
                    x2_change = 0
                if event.key == pygame.K_SPACE:
                    x2_change = 0
                    x1_change = 0
                    y2_change = 0
                    y1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            game_close = True
        x2 += x2_change
        y2 += y2_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head2 = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_Head2.append(x2)
        snake_Head2.append(y2)
        snake_List.append(snake_Head)
        snake_List2.append(snake_Head2)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        if len(snake_List2) > Length_of_snake2:
            del snake_List2[0]

        for x in snake_List2[:-1]:
            if x == snake_Head2:
                game_close = True

        our_snake(snake_block, snake_List)
        our_snake2(snake_block, snake_List2)
        Your_score(Length_of_snake - 1)
        Your_score2(Length_of_snake2 - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        if x2 == foodx and y2 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake2 += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()