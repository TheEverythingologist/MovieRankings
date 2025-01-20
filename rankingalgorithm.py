
class _Competitor:
    """
    A class to represent a competitor in the Elo Rating System.
    """

    def __init__(self, name:str, rating:float):
        """
        Runs at initialization of class object.
        Args:
            name (str): name of the competitor
            rating (float): initial rating of the competitor
        """
        self.name = name
        self.rating = rating
    
    def compareRating(self, opponent: "_Competitor"):
        """
        Compares the two ratings of this competitor and an opponent.

        Args:
            opponent (_Competitor): the player to compare against.
        
        @returns - The expected score between the two players.
        """
        return (1 + 10**((opponent.rating - self.rating)/400.0)) ** -1

class RankingSystem:
    """
    A class that allows for an elo system implementation to rank various competitors.
    """

    def __init__(self, base_rating: float = 2000):
        """
        Initialize the class object.

        Args:
        #####
            base_rating (float): The rating a new player would have.
        """
        self.base_rating: float = base_rating
        self.players: list = []

    def __getPlayerList(self) -> list[_Competitor]:
        """
        Return the implementation's player list.
        @return - the list of all player objects in the implementation.
        """
        return self.players

    def getPlayer(self, name) -> _Competitor:
        """
        Return the competitor in the implementation with the given name.
        @param name - name of the player to return.
        @return - the player with the given name.
        """
        for player in self.players:
            if player.name == name:
                return player
        return None
    
    def contains(self, name) -> bool:
        """
        Returns true if this object contains a player with the given name.
        Otherwise, return false.

        Args:
            name (str): name to check for.
        """
        for player in self.players:
            if player.name == name:
                return True
        return False
    
    def addPlayer(self, name:str, rating:float=None):
        """
        Adds a new player to the implementation.

        Args:
            name (str): The name to identify a specific player.
            rating (float, optional): The player's rating. Defaults to None.
        """
        if rating == None:
            rating = self.base_rating
        self.players.append(_Competitor(name=name, rating=rating))

    def removePlayer(self, name:str):
        """
        Removes a player from the implementation.

        Args:
            name (str): The name to identify a specfic player.
        """
        self.__getPlayerList().remove(self.getPlayer(name=name))

    def recordMatch(self, name1:str, name2:str, winner:str=None, draw:bool=False):
        """
        Should be called after a game is played.

        Args:
            name1 (str): name of the first competitor
            name2 (str): name of the second competitor
            winner (str, optional): name of the winner. Defaults to None.
            draw (bool, optional): was the game a draw. Defaults to False.
        """
        player1 = self.getPlayer(name1)
        player2 = self.getPlayer(name2)

        expected1 = player1.compareRating(player2)
        expected2 = player2.compareRating(player1)
        
        k = len(self.__getPlayerList()) * 42

        rating1 = player1.rating
        rating2 = player2.rating

        if draw:
            score1 = 0.5
            score2 = 0.5
        elif winner == name1:
            score1 = 1.0
            score2 = 0.0
        elif winner == name2:
            score1 = 0.0
            score2 = 1.0
        else:
            raise IndexError('One of the names must be the winner or draw must be True')

        newRating1 = rating1 + k * (score1 - expected1)
        newRating2 = rating2 + k * (score2 - expected2)

        if newRating1 < 0:
            newRating1 = 0
            newRating2 = rating2 - rating1

        elif newRating2 < 0:
            newRating2 = 0
            newRating1 = rating1 - rating2

        player1.rating = newRating1
        player2.rating = newRating2

    def getPlayerRating(self, name:str) -> float:
        """
        Returns the rating of the player with the given name.

        Args:
            name (str): name of the player.

        Returns:
            float: the rating of the player with the given name.
        """
        player = self.getPlayer(name=name)
        return player.rating
    
    def getRatingList(self) -> list[tuple[str, float]]:
        """
        Returns a list of tuples containing the name and ratings.

        Returns:
            list: a tuple containing (name, rating)
        """
        lst = [(player.name, player.rating) for player in self.__getPlayerList]

