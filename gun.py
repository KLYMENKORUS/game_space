import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    """Представляет пушку"""

    def __init__(self, screen):
        super(Gun, self).__init__()
        """Инициализация атрибутов"""
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Флаги перемещения
        self.right = False
        self.left = False

        # Преобразование rect в float
        self.center = float(self.rect.centerx)

    def output(self):
        """Рисует пушку"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновляет позиции"""
        if self.right and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.left and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def created_gun(self):
        """Размешение пушки в нижнем центре экрана"""
        self.center = self.screen_rect.centerx
