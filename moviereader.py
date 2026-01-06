import csv
import requests
from bs4 import BeautifulSoup
from movie_poster import MoviePoster

class MovieReader:
    #TODO There is some kind of issue regarding single quotes. Currently I have to manually add double quotes around the movie title. 
    def __init__(self):
        pass

    def read_listofmovies(self, file_path) -> list[tuple[str, str]]:
        """
        Parse a txt file that contains the list of movies and
        returns a list of tuples containing the names and release years.

        Args:
            file_path (str): Filepath to the list of movies

        Return:
            list[tuple[str, str]]: List of tuples [(Name, Year), ...]
        """
        result = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()  # Remove leading/trailing whitespace
                    if line:  # Skip empty lines
                        try:
                            # Extract the name and year using rstrip and split
                            link = line
                            response = requests.get(link)
                            soup = BeautifulSoup(response.content, 'html.parser')
                            name = soup.find('div', {"class": "details"}).find("span", {"class": "name js-widont prettify"}).text
                            year = soup.find('div', {"class": "details"}).find("span", {"class": "releasedate"}).text
                            result.append((name.strip(), int(year.strip()), link))
                        except ValueError:
                            print(f"Skipping malformed line: {line}")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
        return result
    
    def read_database(self, file_path) -> list[tuple[str, str]]:
        """
        Reads a CSV file with columns "Movie Name" and "Elo Rating"
        and returns a list of tuples in the format [(Name, Year, Elo), ...].

        Args:
            file_path (str): Filepath to the movie database.

        Return:
            list[tuple[str, str]]: List of tuples [(Name, Year, Elo), ...]
        """
        result = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        name = row["MovieName"].strip()
                        year = int(float(row["ReleaseYear"]))
                        elo = int(row["EloRating"])
                        num_comp = int(row["TimesCompeted"])
                        result.append((name, year, elo, num_comp))
                    except (KeyError, ValueError):
                        print(f"Skipping malformed row: {row}")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return result
        

