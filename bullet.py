import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс представляющий снаряд"""

    def __init__(self, screen, gun):
        """Создаем снаряд в текущей позиции"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 30)
        self.color = (180, 230, 29)
        self.speed = 5.0
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """Обновление позиции"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисует снаряд"""
        pygame.draw.rect(self.screen, self.color, self.rect)




