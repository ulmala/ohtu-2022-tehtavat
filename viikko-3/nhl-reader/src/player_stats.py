class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()
        players = filter(
            lambda player: player.nationality == nationality,
            players
        )
        players = list(players)
        players.sort(key=lambda player: player.points, reverse=True)
        return players
