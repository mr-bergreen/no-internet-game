# no-internet-game - lesson 6

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
  state = "standing"
  velocity = 0

  def jump(self):
    self.state = "jumping"
    self.velocity = 18

  def stand(self):
    self.state = "standing"
    self.velocity = 0

  def update(self):
    self.velocity -= 1
    self.y -= self.velocity

    if self.y >= 240 - self.height/2:
      self.velocity = 0
      self.state = "standing"
      self.y = 240 - self.height/2

  def draw(self):
    pygame.draw.rect(screen, RED, (self.x, self.y - self.height/2, self.width, self.height))
  
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
    
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
          if player.state == "standing":
            player.jump()

  # Update
  player.update()

  # Draw
  screen.fill(BLACK)
  
  pygame.draw.line(screen, WHITE, (0,HEIGHT/2), (WIDTH,HEIGHT/2))
  player.draw()

  # Load
  pygame.display.flip()
  clock.tick(60)