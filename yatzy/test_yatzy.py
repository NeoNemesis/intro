import random
import unittest

from game import MAX_PLAYERS, Game
from scoring import CATEGORIES, score


class TestScore(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(score("treor", [3, 3, 1, 3, 6]), 9)
        self.assertEqual(score("sexor", [1, 2, 3, 4, 5]), 0)

    def test_pairs(self):
        self.assertEqual(score("ett_par", [2, 2, 5, 5, 1]), 10)
        self.assertEqual(score("tva_par", [2, 2, 5, 5, 1]), 14)
        self.assertEqual(score("tva_par", [2, 2, 2, 5, 1]), 0)
        self.assertEqual(score("tva_par", [4, 4, 4, 4, 1]), 0)

    def test_of_a_kind(self):
        self.assertEqual(score("tretal", [4, 4, 4, 2, 1]), 12)
        self.assertEqual(score("fyrtal", [6, 6, 6, 6, 6]), 24)
        self.assertEqual(score("fyrtal", [6, 6, 6, 1, 1]), 0)

    def test_straights(self):
        self.assertEqual(score("liten_stege", [5, 3, 1, 2, 4]), 15)
        self.assertEqual(score("stor_stege", [6, 3, 5, 2, 4]), 20)
        self.assertEqual(score("stor_stege", [1, 2, 3, 4, 5]), 0)

    def test_full_house(self):
        self.assertEqual(score("kak", [3, 3, 5, 5, 5]), 21)
        self.assertEqual(score("kak", [5, 5, 5, 5, 5]), 0)

    def test_chance_and_yatzy(self):
        self.assertEqual(score("chans", [1, 2, 3, 4, 6]), 16)
        self.assertEqual(score("yatzy", [2, 2, 2, 2, 2]), 50)
        self.assertEqual(score("yatzy", [2, 2, 2, 2, 1]), 0)


class TestGame(unittest.TestCase):
    def test_player_limits(self):
        with self.assertRaises(ValueError):
            Game([])
        with self.assertRaises(ValueError):
            Game(["x"] * (MAX_PLAYERS + 1))

    def test_max_three_rolls(self):
        game = Game(["A"], random.Random(1))
        game.roll()
        game.roll()
        game.roll()
        with self.assertRaises(RuntimeError):
            game.roll()

    def test_held_dice_stay(self):
        game = Game(["A"], random.Random(1))
        game.roll()
        before = list(game.dice.values)
        game.dice.hold_only([0, 2])
        game.roll()
        self.assertEqual(game.dice.values[0], before[0])
        self.assertEqual(game.dice.values[2], before[2])

    def test_full_game(self):
        game = Game(["A", "B", "C", "D", "E", "F"], random.Random(7))
        while not game.is_over():
            game.roll()
            game.choose(game.available_categories()[0])
        for player in game.players:
            self.assertEqual(len(player.scores), len(CATEGORIES))
        self.assertTrue(len(game.winners()) >= 1)

    def test_bonus(self):
        game = Game(["A"])
        player = game.players[0]
        player.scores = {"ettor": 3, "tvaor": 6, "treor": 9,
                         "fyror": 12, "femmor": 15, "sexor": 18}
        self.assertEqual(player.bonus(), 50)
        self.assertEqual(player.total(), 63 + 50)


if __name__ == "__main__":
    unittest.main()
