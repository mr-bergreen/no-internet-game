# no-internet-game - lesson 4

import pygame
from pygame.locals import *
import sys

#------------ INIT ------------#
pygame.init()

WIDTH = 480
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#------------ CLASSES ------------#
class Player():
  x = 50
  y = HEIGHT/2
  width = 50
  height = 50

  def draw(self):
    pygame.draw.rect(screen, RED, (self.x, self.y - self.height, self.width, self.height))
  
#------------ COLORS ------------#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#------------ OBJECTS ------------#
player = Player()

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
  player.draw()

  # Load
  pygame.display.flip()
  clock.tick(60)