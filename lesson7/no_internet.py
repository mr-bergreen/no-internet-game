# no-internet-game - lesson 7

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

class Obstacle():
  x = WIDTH + 25
  y = HEIGHT/2
  width = 25
  height = 25
  velocity = 5

  def update(self):
    self.x -= self.velocity

    if self.x <= 0 - self.width:
      self.x = WIDTH + 25
  
  def draw(self):
    pygame.draw.rect(screen, GREEN, (self.x, self.y - self.height, self.width, self.height))

#------------ COLORS ------------#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#------------ OBJECTS ------------#
player = Player()
obstacle = Obstacle()

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
  obstacle.update()

  # Draw
  screen.fill(BLACK)
  
  pygame.draw.line(screen, WHITE, (0,HEIGHT/2), (WIDTH,HEIGHT/2))
  player.draw()
  obstacle.draw()

  # Load
  pygame.display.flip()
  clock.tick(60)