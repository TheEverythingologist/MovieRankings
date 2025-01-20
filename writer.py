import pandas as pd
from movie import Movie
from rankingalgorithm import _Competitor

class MovieWriter:
    def __init__(self):
        pass

    def write_to_csv(self, dataframe: pd.DataFrame, file_name:str):
        dataframe.to_csv(file_name, sep=",", encoding='utf-8', index=False)

    def add_to_csv(self, dataframe: pd.DataFrame, file_name:str):
        dataframe.to_csv(file_name, mode='a', header=False, index=False)

    def generate_new_movie_df(self, list_of_new_movies: list[tuple[str, str]]):
        _df = pd.DataFrame(list_of_new_movies, columns=["MovieName", "ReleaseYear"])
        _df["EloRating"] = range(1000 + len(_df)//2 + 1, 1000 - len(_df)//2, -1)
        _df["TimesCompeted"] = 0
        _df.insert(0, "Rank", range(1, len(_df) + 1))  # Add "Rank" as the leftmost column
        return _df
    
    def update_database(self, movie_df:pd.DataFrame, movie1:_Competitor, movie2:_Competitor):
        criteria1 = ((movie_df["MovieName"] == movie1.movie_name) & (movie_df["ReleaseYear"] == int(movie1.movie_year)))
        criteria2 = ((movie_df["MovieName"] == movie2.movie_name) & (movie_df["ReleaseYear"] == int(movie2.movie_year)))
        movie_df.loc[criteria1, "EloRating"] = int(movie1.rating)
        movie_df.loc[criteria1, "TimesCompeted"] = movie1.num_competitions
        # Update Movie 2
        movie_df.loc[criteria2, "EloRating"] = int(movie2.rating)
        movie_df.loc[criteria2, "TimesCompeted"] = movie2.num_competitions
        # Update the rank column
        movie_df = movie_df.sort_values(by="EloRating", ascending=False)
        movie_df["Rank"] = range(1, len(movie_df) + 1)
        movie_df["ReleaseYear"] = movie_df["ReleaseYear"].astype(float)
        movie_df["ReleaseYear"] = movie_df["ReleaseYear"].astype("Int64")
        return movie_df
