MIDPOINT_SCORE = 2000

class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year
        self.initial_score = MIDPOINT_SCORE

    #TODO Add ability to get rankings from various websites like Letterboxd, IMDB, Rotten Tomatoes, etc.

    def getRottenTomatoesLink(self):
        pass

    def getRottenTomatoesScore(self):
        pass

    def getIMDBLink(self):
        pass

    def getIMDBScore(self):
        pass

    def getLetterboxdLink(self):
        pass

    def getLetterboxdScore(self):
        pass