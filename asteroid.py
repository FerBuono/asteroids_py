import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
  containers = ()
  
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def draw(self, screen):
    pygame.draw.circle(screen, "gray", self.position, self.radius, 2)
    
  def update(self, dt: float):
    self.position += self.velocity * dt