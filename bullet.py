import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manege bullets fired from the ship"""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load bullet image and set correct position
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.image.blit(self.image, self.rect)
