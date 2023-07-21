from lib import Snake
snake = Snake()

import pygame

show_border = False
speed = 0.2
tail_size = 24
screen_height = snake.height * (tail_size + (1 if show_border else 0))
screen_width = snake.width * (tail_size + (1 if show_border else 0))

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height,))

colors = (
    (100, 180, 100,),
    (0, 56, 0,),
    (220, 220, 0,),
)

done = False

import time
from lib.direction import Direction

directions = {
    pygame.K_UP: Direction.NORTH.value,
    pygame.K_RIGHT: Direction.EAST.value,
    pygame.K_DOWN: Direction.SOUTH.value,
    pygame.K_LEFT:Direction.WEST.value,
}

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYUP:
            if event.key in directions.keys():
                snake.change_direction(directions[event.key])

    try:
        snake.step()
    except Exception as e:
        print(e)
        snake = Snake()

    for r in range(0, snake.height):
        for c in range(0, snake.width):
            x = c * (tail_size + (1 if show_border else 0))
            y = r * (tail_size + (1 if show_border else 0))
            pygame.draw.rect(screen, colors[snake.at(row=r, col=c)], pygame.Rect(x, y, tail_size, tail_size))

    pygame.display.set_caption(f'Yet Another Snake Game ({len(snake.snake)})')
    pygame.display.update()
    time.sleep(speed)
