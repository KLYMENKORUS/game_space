import pygame, sys, time
from bullet import Bullet
from ufo import Ufo


def events(screen, gun, bullets):
    """Обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.right = True
            # влево
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.left = True
            # выстрел
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.right = False
            # влево
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.left = False


def update(bg_color, screen, stats, sc, gun, ufos, bullets):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    ufos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, ufos, bullets):
    """Обновление позиции и удаление снаряда """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)
    if collisions:
        for ufos in collisions.values():
            stats.score += 10 * len(ufos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.images_guns()
    if len(ufos) == 0:
        bullets.empty()
        create_fleet(screen, ufos)


def gun_kill(stats, screen, sc,  gun, ufos, bullets):
    """Коллизия пушки с флотом"""
    if stats.guns_left > 0:
        stats.guns_left -= 1

        sc.images_guns()
        ufos.empty()
        bullets.empty()

        create_fleet(screen, ufos)
        gun.created_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_ufos(stats, screen, sc, gun, ufos, bullets):
    """Обновление позициий пришельцев"""
    ufos.update()
    if pygame.sprite.spritecollideany(gun, ufos):
        gun_kill(stats, screen, sc, gun, ufos, bullets)
    ufos_check(stats, screen, sc, gun, ufos, bullets)


def ufos_check(stats, screen, sc, gun, ufos, bullets):
    """Добрались ли пришельци к нижнему краю экрана"""
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, ufos, bullets)
            break


def create_fleet(screen, ufos):
    """Создание флота"""
    ufo = Ufo(screen)
    ufo_width = ufo.rect.width
    number_ufo_x = int((800 - 2 * ufo_width) / ufo_width)

    ufo_height = ufo.rect.height
    number_ufo_y = int((650 - 100 - 2 * ufo_height) / ufo_height)

    for row_ufo in range(number_ufo_y-1):
        for ufo_number in range(number_ufo_x):
            ufo = Ufo(screen)

            ufo.x = ufo_width + ufo_width * ufo_number
            ufo.y = ufo_height + ufo_height * row_ufo

            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.rect.height + ufo.rect.height * row_ufo

            ufos.add(ufo)


def check_high_score(stats, sc):
    """Проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()

        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))
