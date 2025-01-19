import pandas as pd

class Writer:
    def __init__(self):
        pass

    def write_to_csv(self, dataframe: pd.DataFrame, file_name:str):
        dataframe.to_csv(file_name, sep=", ", encoding='utf-8')

    def add_to_csv(self, dataframe: pd.DataFrame, file_name:str):
        dataframe.to_csv(file_name, mode='a', header=False)

    def generate_new_movie_dataframe(self, list_of_new_movies: list[tuple[str, str]]):
        _df = pd.DataFrame(list_of_new_movies, columns=["Movie Name", "Release Year"])
        _df["Elo Rating"] = 2000
        _df["Times Competed"] = 0
        return _df