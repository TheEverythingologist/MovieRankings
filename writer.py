import pandas as pd
from movie import Movie

class MovieWriter:
    def __init__(self):
        pass

    def write_to_csv(self, dataframe: pd.DataFrame, file_name:str):
        dataframe.to_csv(file_name, sep=",", encoding='utf-8')

    def add_to_csv(self, dataframe: pd.DataFrame, file_name:str):
        dataframe.to_csv(file_name, mode='a', header=False)

    def generate_new_movie_dataframe(self, list_of_new_movies: list[tuple[str, str]]):
        _df = pd.DataFrame(list_of_new_movies, columns=["Movie Name", "Release Year"])
        _df["Elo Rating"] = range(2000 + len(_df)//2 + 1, 2000 - len(_df)//2, -1)
        _df["Times Competed"] = 0
        _df.insert(0, "Rank", range(1, len(_df) + 1))  # Add "Rank" as the leftmost column
        return _df
    
    def update_database(self, movie1:Movie, movie2:Movie):
        # Update the elo ranking of both movies
        # Update the rank column
        pass
