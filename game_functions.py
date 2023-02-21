import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key down"""
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullet_limit:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key up"""
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_up = False
    elif event.key == pygame.K_s:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
