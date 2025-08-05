import re
import requests
import bs4

MIDPOINT_SCORE = 1000

class Movie:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year
        self.initial_score = MIDPOINT_SCORE
        # TODO make it so it doesn't have to check this every single time
        self.letterboxd_link = self.getLetterboxdLink()

    #TODO Add ability to get rankings from various websites like Letterboxd, IMDB, Rotten Tomatoes, etc.

    # def getIMDBLink(self):
    #     pass

    # def getIMDBScore(self):
    #     pass

    def getLetterboxdLink(self):
        name_in_link = slugify(self.name)
        link = f"https://letterboxd.com/film/{name_in_link}/"
        is_link_valid = check_letterboxd_link(link)
        print(f"{is_link_valid}")

        # TODO add this to the database

    def getLetterboxdScore(self):
        pass

    def getmovieposter(self):
        pass

    def __eq__(self, other: "Movie"):
        if self.name == other.name and self.release_year == other.release_year:
            return True
        else:
            return False
        

def slugify(text: str) -> str:
    # Replace non-alphanumeric characters with dashes
    text = re.sub(r'[^a-zA-Z0-9]', '-', text)
    # Replace multiple dashes with a single dash
    text = re.sub(r'-+', '-', text)
    # Strip leading/trailing dashes and lowercase
    return text.strip('-').lower()


def check_letterboxd_link(link: str) -> bool:
    # Return True if the link is good. False if the link is bad.
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    error_message = soup.find("body", {"class": "error message-dark"})
    if error_message is None:
        return True
    else:
        return False
    
if __name__ == "__main__":
    dumm = Movie(name="The SocialNetwork", release_year=2010)