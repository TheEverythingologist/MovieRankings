import pandas as pd
from movie import Movie
from rankingalgorithm import _Competitor

class MovieWriter:
    def __init__(self):
        pass

    def write_to_csv(self, dataframe: pd.DataFrame, file_name:str):
        dataframe.to_csv(file_name, sep=",", encoding='utf-8')

    def add_to_csv(self, dataframe: pd.DataFrame, file_name:str):
        dataframe.to_csv(file_name, mode='a', header=False)

    def generate_new_movie_df(self, list_of_new_movies: list[tuple[str, str]]):
        _df = pd.DataFrame(list_of_new_movies, columns=["Movie Name", "Release Year"])
        _df["Elo Rating"] = range(1000 + len(_df)//2 + 1, 1000 - len(_df)//2, -1)
        _df["Times Competed"] = 0
        _df.insert(0, "Rank", range(1, len(_df) + 1))  # Add "Rank" as the leftmost column
        return _df
    
    def update_database(self, movie_df:pd.DataFrame, movie1:_Competitor, movie2:_Competitor):
        movie_df.loc[((movie_df["Movie Name"] == movie1.movie_name) & (movie_df["Release Year"] == movie1.movie_year)), "Elo Rating"] = int(movie1.rating)
        movie_df.loc[((movie_df["Movie Name"] == movie1.movie_name) & (movie_df["Release Year"] == movie1.movie_year)), "Times Competed"] = movie1.num_competitions
        # Update Movie 2
        movie_df.loc[((movie_df["Movie Name"] == movie2.movie_name) & (movie_df["Release Year"] == movie2.movie_year)), "Elo Rating"] = int(movie2.rating)
        movie_df.loc[((movie_df["Movie Name"] == movie2.movie_name) & (movie_df["Release Year"] == movie2.movie_year)), "Times Competed"] = movie2.num_competitions
        # Update the rank column
        movie_df.sort_values("Elo Rating")
        return movie_df
