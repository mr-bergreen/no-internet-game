# no-internet-game - lesson 3

import pygame
from pygame.locals import *
import sys

#------------ INIT ------------#
pygame.init()

WIDTH = 480
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#------------ COLORS ------------#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#------------ Game Loop ------------#
while True:
  
  # Event Loop
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Update

  # Draw
  screen.fill(BLACK)
  
  pygame.draw.line(screen, WHITE, (0,HEIGHT/2), (WIDTH,HEIGHT/2))
  pygame.draw.rect(screen, RED, (50, HEIGHT/2 - 50, 50, 50))

  # Load
  pygame.display.flip()
  clock.tick(60)