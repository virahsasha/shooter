import pygame

# ініціалізуємо pygame
pygame.init()

# встановлюємо розмір вікна
screen = pygame.display.set_mode((800, 600))

# створюємо гравця
player = pygame.Rect(400, 500, 40, 40)

# створюємо ворогів
enemies = []
for i in range(5):
    enemy = pygame.Rect(100 * i, 50, 40, 40)
    enemies.append(enemy)

# створюємо кулі
bullets = []

# головний цикл гри
while True:
    # обробляємо події
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx, player.top, 5, 10)
                bullets.append(bullet)

    # переміщуємо гравця
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player.right < 800:
        player.move_ip(5, 0)

    # переміщуємо кулі
    for bullet in bullets:
        bullet.move_ip(0, -10)
        if bullet.top < 0:
            bullets.remove(bullet)

    # переміщуємо ворогів
    for enemy in enemies:
        enemy.move_ip(2, 0)
        if enemy.right > 800 or enemy.left < 0:
            enemies.remove(enemy)

    # перевіряємо стику кулі з ворогами
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)

    # очищуємо екран
    screen.fill((0, 0, 0))

    # малюємо гравця
    pygame.draw.rect(screen, (255, 255, 255), player)

    # малюємо ворогів
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

    # малюємо кулі
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)

    # оновлюємо екран
    pygame.display.update()
