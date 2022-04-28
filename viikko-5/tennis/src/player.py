class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    def add_score(self):
        self._score += 1

    def name(self):
        return self._name

    def score(self):
        return self._score

    def __str__(self):
        return self._name