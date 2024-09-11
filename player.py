import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
  containers = ()

  def __init__(self, x: int, y: int):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    
    for group in self.containers:
      group.add(self)
    
  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
  def rotate(self, dt: float):
    self.rotation += PLAYER_TURN_SPEED * dt
  
  def triangle(self) -> list[pygame.Vector2]:
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def move(self, dt: float):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt
  
  def update(self, dt: float):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
      self.rotate(-dt)
      
    if keys[pygame.K_d]:
      self.rotate(dt)
      
    if keys[pygame.K_w]:
      self.move(dt)
      
    if keys[pygame.K_s]:
      self.move(-dt)
      
      
    