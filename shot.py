import pygame
from circleshape import CircleShape

class Shot(CircleShape):
  containers = ()
  
  def __init__(self, x: int, y: int, radius: int):
    super().__init__(x, y, radius)
    
  def draw(self, screen):
    pygame.draw.circle(screen, "red", self.position, self.radius)
    
  def update(self, dt: float):
    self.position += self.velocity * dt