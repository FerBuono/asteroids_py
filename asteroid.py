import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
  containers = ()
  
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    rand_angle = random.uniform(20,50)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
        
    a = Asteroid(self.position.x, self.position.y, new_radius)
    a.velocity = self.velocity.rotate(rand_angle) * 1.2
    b = Asteroid(self.position.x, self.position.y, new_radius)
    b.velocity = self.velocity.rotate(-rand_angle) * 1.2
    
  
  def draw(self, screen):
    pygame.draw.circle(screen, "gray", self.position, self.radius, 2)

  def update(self, dt: float):
    self.position += self.velocity * dt