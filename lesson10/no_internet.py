# no-internet-game - lesson 10

import pygame
from pygame.locals import *
import sys
import random

#------------ INIT ------------#
pygame.init()

WIDTH = 480
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#------------ FUNCTIONS ------------#
def change_obstacle():
  obstacles = (Obstacle, TallObstacle, WideObstacle)
  obstacle = random.choice(obstacles)
  return obstacle()

def draw_score(score):
  font = pygame.font.Font('PressStart2P.ttf', 16)
  render = font.render('Score = ' + str(score), True, WHITE)
  screen.blit(render, (10, 10))

#------------ CLASSES ------------#
class Player():
  x = 50
  y = HEIGHT/2
  width = 50
  height = 50
  state = "standing"
  velocity = 0
  rect = pygame.Rect(x, y - height, width, height)

  def is_collided_with(self, obstacle):
    return self.rect.colliderect(obstacle.rect)

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
    self.rect = pygame.Rect(self.x, self.y - self.height/2, self.width, self.height)
    pygame.draw.rect(screen, RED, self.rect)

class Obstacle():
  x = WIDTH + 25
  y = HEIGHT/2
  width = 25
  height = 25
  velocity = 5
  rect = pygame.Rect(x, y - height, width, height)

  def update(self):
    global obstacle, score

    self.x -= self.velocity

    if self.x <= 0 - self.width:
      self.x = WIDTH + 25
      obstacle = change_obstacle()
      score += 1

  def draw(self):
    self.rect = pygame.Rect(self.x, self.y - self.height, self.width, self.height)
    pygame.draw.rect(screen, GREEN, self.rect)

class TallObstacle(Obstacle):
  height = 50

class WideObstacle(Obstacle):
  width = 50

#------------ COLORS ------------#
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#------------ OBJECTS ------------#
player = Player()
obstacle = change_obstacle()

score = 0

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
  if player.is_collided_with(obstacle):
    print("collided")
  else:
    player.update()
    obstacle.update()

  # Draw
  screen.fill(BLACK)

  draw_score(score)
  
  pygame.draw.line(screen, WHITE, (0,HEIGHT/2), (WIDTH,HEIGHT/2))
  player.draw()
  obstacle.draw()

  # Load
  pygame.display.flip()
  clock.tick(60)