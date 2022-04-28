class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2       

    def won_point(self, player):
        player.add_score()

    def _game_is_tie(self):
        if self.player1.score() == self.player2.score():
            return True
        return False

    def _one_player_has_over_four_points(self):
        if self.player1.score() >= 4 or self.player2.score() >= 4:
            return True
        return False

    def _get_score_str(self, score):
        if score == 0: return "Love"
        elif score == 1: return "Fifteen"
        elif score == 2: return "Thirty"
        elif score == 3: return "Forty"

    def _get_score_in_tie(self):
        if self.player1.score() <= 3:
            return f"{self._get_score_str(self.player1.score())}-All"
        return "Deuce"

    def _one_player_has_advantage(self):
        if self.player1.score() - self.player2.score() in [1, -1]:
            return True
        return False

    def _get_advantaged_player(self):
        if self.player1.score() - self.player2.score() == 1:
            return self.player1.name()
        return self.player2.name()

    def _get_winner(self):
        if self.player1.score() - self.player2.score() >= 2:
            return self.player1.name()
        return self.player2.name()

    def get_score(self):
        if self._game_is_tie():
            return self._get_score_in_tie()

        elif self._one_player_has_over_four_points():

            if self._one_player_has_advantage():
                return f"Advantage {self._get_advantaged_player()}"

            return f"Win for {self._get_winner()}"

        return f"{self._get_score_str(self.player1.score())}-{self._get_score_str(self.player2.score())}"
