from pydoc import plain
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_correc_player(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(str(player), str(Player("Semenko", "EDM", 4, 12)))

    def test_search_returns_none_if_player_not_found(self):
        self.assertIsNone(self.statistics.search("lol"))

    def test_team_returns_correct_list_of_players(self):
        players = [str(player) for player in self.statistics.team("EDM")]
        self.assertEqual(
            players,
            [
                str(Player("Semenko", "EDM", 4, 12)),
                str(Player("Kurri",   "EDM", 37, 53)),
                str(Player("Gretzky", "EDM", 35, 89))
            ]
        )

    def test_top_scorers_returns_correct_players(self):
        players = [str(player) for player in self.statistics.top_scorers(1)]
        self.assertEqual(
            players,
            [
                str(Player("Gretzky", "EDM", 35, 89)),
                str(Player("Lemieux", "PIT", 45, 54))
            ]
        )