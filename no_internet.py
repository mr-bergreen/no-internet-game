# starter template for the no-internet-game

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

  # Load
  pygame.display.flip()
  clock.tick(60)