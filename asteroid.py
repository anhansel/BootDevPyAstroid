import random

import pygame

from circleshape import CircleShape

from constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        split1 = self.velocity.rotate(angle)
        split2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = split1 * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = split2 * 1.2