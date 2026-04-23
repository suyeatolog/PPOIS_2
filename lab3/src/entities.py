import pygame

class Paddle(pygame.Rect):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height)
        self.color = color
        self.base_speed = speed
        self.speed = speed
        self.vel_y = 0

    def reset(self):
        self.speed = self.base_speed

    def move(self):
        self.y += self.vel_y
        self.y = max(0, min(self.y, 800 - self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

class Ball(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color
        self.speed_x = 0
        self.speed_y = 0
        self.hit_counter = 0

    def reset(self, dir_x=1):
        self.center = (700, 400)
        self.speed_x = 6 * dir_x
        self.speed_y = 6
        self.hit_counter = 0

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.top <= 0 or self.bottom >= 800:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self)