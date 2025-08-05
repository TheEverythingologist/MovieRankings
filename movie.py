MIDPOINT_SCORE = 2000

class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year
        self.initial_score = MIDPOINT_SCORE

    #TODO Add ability to get rankings from various websites like Letterboxd, IMDB, Rotten Tomatoes, etc.

    def getIMDBLink(self):
        pass

    def getIMDBScore(self):
        pass

    def getLetterboxdLink(self):
        pass

    def getLetterboxdScore(self):
        pass

    def getmovieposter(self):
        pass

    def __eq__(self, other: "Movie"):
        if self.name == other.name and self.release_year == other.release_year:
            return True
        else:
            return False