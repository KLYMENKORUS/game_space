import pygame.font
from gun import Gun
from pygame.sprite import Group


class Scores():
    """Вывод игровой инфорации"""
    def __init__(self, screen, stats):
        """Инициализазция подсчета очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (180, 230, 29)
        self.font = pygame.font.SysFont('Arial', 36)
        self.image_score()
        self.image_high_score()
        self.images_guns()

    def image_score(self):
        """Преобразование счета в изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 10

    def image_high_score(self):
        """Преобразовывает рекорд в графическое изображение"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.score_rect.centerx - 300
        self.high_score_rect.top = self.score_rect.top

    def images_guns(self):
        """Количество жизней"""
        self.guns = Group()

        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)


