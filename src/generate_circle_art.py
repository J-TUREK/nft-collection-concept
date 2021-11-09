import random
import time
import sys
import pygame
import math
import pandas as pd

pygame.init()


def get_random_colour():
    '''
    Generate a random RGB colour
    '''

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def get_random_rectangle():
    '''
    rectangle = (top left x, top left y, width, height)
    '''

    x_pos = random.randint(1, WIDTH - WIDTH/4)
    y_pos = random.randint(1, HEIGHT - HEIGHT/4)
    width = random.randint(10, WIDTH - x_pos)
    height = random.randint(10, HEIGHT - y_pos)

    return (x_pos, y_pos, width, height)


PI = math.pi
SIZE = WIDTH, HEIGHT = 1500, 1500
screen = pygame.display.set_mode(SIZE)
IMAGES = 100
x = 0

while x < IMAGES:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(get_random_colour())

    circles = random.randint(120, 150)

    for i in range(circles):

        start_angle = random.random() * PI
        end_angle = random.random() * PI

        pygame.draw.arc(screen, get_random_colour(),
                        get_random_rectangle(), start_angle, end_angle, random.randint(1, 3))

    pygame.display.flip()

    time.sleep(0.2)  # Display the beautiful artwork

    x += 1
    pygame.image.save(screen, f"collection1/circasso{x}.jpeg")
    print(x)
