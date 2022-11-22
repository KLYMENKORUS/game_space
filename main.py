import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 650))
    pygame.display.set_caption('Game space')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    ufos = Group()
    bullets = Group()
    controls.create_fleet(screen, ufos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update()
            controls.update(bg_color, screen, stats, sc, gun, ufos, bullets)
            controls.update_bullets(screen, stats, sc, ufos, bullets)
            controls.update_ufos(stats, screen, sc, gun, ufos, bullets)


run()

