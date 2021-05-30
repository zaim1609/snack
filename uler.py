import pygame
import random

pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

WIDTH = 1330
HEIGHT = 750

snake_radius = 10
snake_size = snake_radius * 2

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.mouse.set_visible(False)

# display_surface  = pygame.display.set_mode((WIDTH,HEIGHT))
display_surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Snake')

font = pygame.font.Font('FreeSansBold.ttf', 30)

def message(input_text, color):
    text = font.render(input_text, True, color)
    text_rect = text.get_rect(center = (WIDTH / 2, HEIGHT / 2))
    display_surface.blit(text, text_rect)

def snake(snake_radius, snake_List):
    for i in snake_List:
        pygame.draw.circle(display_surface, white, [i[0], i[1]], snake_radius)

def score(score):
    value = font.render("Score : " +str(score), True, white)
    display_surface.blit(value,[10,10])


clock = pygame.time.Clock()

def game():
    game_over = False
    game_close = False
    x1 = (((WIDTH // snake_size) // 2) * snake_size) - snake_radius
    y1 = (((HEIGHT // snake_size) // 2) * snake_size) - snake_radius

    x1_change = 0
    y1_change = 0

    snake_List = []
    snake_length = 1

    food_x = round(random.randrange(snake_radius, (WIDTH // snake_size) * snake_size, snake_size))
    food_y = round(random.randrange(snake_radius, (HEIGHT // snake_size) * snake_size, snake_size))

    while not game_over:

        while game_close == True:
            screen.fill((black))
            message("Game Over press Q to Quit or R to restart", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True
                    if event.key == pygame.K_r:
                        game()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
             game_close= True

        x1 += x1_change
        y1 += y1_change

        screen.fill((black))

        pygame.draw.circle(display_surface, green, [food_x,food_y], snake_radius)
        snake_List.append((x1,y1))

        if len(snake_List) > snake_length:
            del snake_List[0]

        snake_head = []
        snake_head.append((x1, y1))

        for i in snake_List[:-1]:
            for j in snake_head:
                if i == j:
                    game_close = True


        snake(snake_radius,snake_List)
        score(snake_length - 1)

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(snake_radius, WIDTH - snake_radius, snake_size))
            food_y = round(random.randrange(snake_radius, HEIGHT - snake_radius, snake_size))
            snake_length += 1


        pygame.display.update()
        clock.tick(10)
game()