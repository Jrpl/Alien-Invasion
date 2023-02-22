import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        # Initialize alien and starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien position
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw alien
        self.screen.blit(self.image, self.rect)
