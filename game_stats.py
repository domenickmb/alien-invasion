import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, game):
        """Initialize statistics."""
        self.settings = game.settings
        self.reset_stats()

        # Start game in an inactive state
        self.game_active = False
        
        # High score should never be reset.
        self.high_score_file = 'high_score.json'
        self.high_score = self._read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _read_high_score(self):
        """Read high score from a file if it exists."""
        try:
            with open(self.high_score_file) as f:
                high_score = json.load(f)
        except FileNotFoundError:
            high_score = 0

        return high_score

    def write_high_score(self):
        """Write high score to a file."""
        with open(self.high_score_file, 'w') as f:
            json.dump(self.high_score, f)
