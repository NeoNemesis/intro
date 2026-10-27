import random

from scoring import BONUS_LIMIT, BONUS_POINTS, CATEGORIES, UPPER, score

NUM_DICE = 5
MAX_ROLLS = 3
MIN_PLAYERS = 1
MAX_PLAYERS = 6

# Spellogiken skriver aldrig ut något och läser aldrig input.
# All kommunikation med användaren sköts av en view (se terminal_view.py),
# så att samma spel kan visas i terminalen eller i ett grafiskt fönster.


class Dice:
    def __init__(self, rng=None):
        self.rng = rng if rng is not None else random.Random()
        self.values = [1] * NUM_DICE
        self.held = [False] * NUM_DICE

    def roll(self):
        for i in range(NUM_DICE):
            if not self.held[i]:
                self.values[i] = self.rng.randint(1, 6)

    def hold_only(self, positions):
        self.held = [i in positions for i in range(NUM_DICE)]

    def toggle(self, position):
        self.held[position] = not self.held[position]

    def release_all(self):
        self.held = [False] * NUM_DICE


class Player:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def has_used(self, category):
        return category in self.scores

    def upper_sum(self):
        return sum(self.scores.get(key, 0) for key in UPPER)

    def bonus(self):
        return BONUS_POINTS if self.upper_sum() >= BONUS_LIMIT else 0

    def total(self):
        return sum(self.scores.values()) + self.bonus()

    def is_done(self):
        return len(self.scores) == len(CATEGORIES)


class Game:
    def __init__(self, names, rng=None):
        if not MIN_PLAYERS <= len(names) <= MAX_PLAYERS:
            raise ValueError(f"Antal spelare måste vara {MIN_PLAYERS}-{MAX_PLAYERS}")
        self.players = [Player(name) for name in names]
        self.dice = Dice(rng)
        self.current = 0
        self.rolls_left = MAX_ROLLS

    def current_player(self):
        return self.players[self.current]

    def has_rolled(self):
        return self.rolls_left < MAX_ROLLS

    def can_roll(self):
        return self.rolls_left > 0 and not self.is_over()

    def roll(self):
        if not self.can_roll():
            raise RuntimeError("Inga slag kvar")
        if not self.has_rolled():
            self.dice.release_all()
        self.dice.roll()
        self.rolls_left -= 1

    def available_categories(self):
        player = self.current_player()
        return [key for key, name in CATEGORIES if not player.has_used(key)]

    def preview(self, category):
        return score(category, self.dice.values)

    def choose(self, category):
        if not self.has_rolled():
            raise RuntimeError("Du måste slå minst en gång först")
        if category not in self.available_categories():
            raise ValueError("Kategorin är redan använd")
        points = self.preview(category)
        self.current_player().scores[category] = points
        self.next_turn()
        return points

    def next_turn(self):
        self.current = (self.current + 1) % len(self.players)
        self.rolls_left = MAX_ROLLS
        self.dice.release_all()

    def is_over(self):
        return all(player.is_done() for player in self.players)

    def winners(self):
        best = max(player.total() for player in self.players)
        return [player for player in self.players if player.total() == best]
