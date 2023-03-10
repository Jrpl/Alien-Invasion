import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        # Initialize the ship and set its starting position
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal for ship center
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship position based on movement flag.
        Update ship center not rect."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerX += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerX -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centerY -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.centerY += self.ai_settings.ship_speed_factor

        # Update rect object from center
        self.rect.centerx = self.centerX
        self.rect.centery = self.centerY

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
