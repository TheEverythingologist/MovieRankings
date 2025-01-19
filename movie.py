MIDPOINT_SCORE = 2000

class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year
        self.initial_score = MIDPOINT_SCORE