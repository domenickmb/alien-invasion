import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings

        # Screen size of window mode
        self.screen_width = 1200
        self.screen_height = 800

        # The flag variable to run the game in full screen or window mode
        # defaults to window mode; set it to True to run in full screen
        self.fullscreen = False

        if self.fullscreen:
            self.background_image = pygame.image.load('images/space.bmp')
        else:
            self.background_image = pygame.image.load('images/space_1200x800.bmp')

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullets_allowed = 8

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1.0
        self.alien_points = 50
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
