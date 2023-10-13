"""
ADS Final Project
=================
A black-jack implementation in Python.
Using:
+ Pygame
"""

import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Black Jack')
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
