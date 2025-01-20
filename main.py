import random
import pandas as pd
from movie import Movie
from rankingalgorithm import RankingSystem, _Competitor
from moviereader import MovieReader
from writer import MovieWriter
from interface import Interface

def main():
    # Read in movies list
    path_to_list_of_movies = "C:/Users/TKD12/OneDrive/Desktop/CodingRepos/MovieRanking/data/list_of_movies.txt"
    movie_reader = MovieReader()
    new_movies_list = movie_reader.read_listofmovies(file_path=path_to_list_of_movies)

    # Add new movies to the database
    path_to_database = "C:/Users/TKD12/OneDrive/Desktop/CodingRepos/MovieRanking/data/database.csv"
    movie_writer = MovieWriter()
    movie_df = movie_writer.generate_new_movie_df(list_of_new_movies=new_movies_list)
    if len(new_movies_list) > 0:
        movie_writer.add_to_csv(dataframe=movie_df, file_name=path_to_database)

    # Setup the elo system
    movie_data_from_csv = movie_reader.read_database("C:/Users/TKD12/OneDrive/Desktop/CodingRepos/MovieRanking/data/database.csv")
    elo_system = RankingSystem()
    elo_system.addMultiplePlayers(movie_data_from_csv)
    movie_df = pd.read_csv(path_to_database)

    # Initialize interface
    interface = Interface()
    # Begin loop
    while True:
        # Draw two movies from the database, prioritizing ones with fewer competitions
        competing_movies: list[_Competitor] = elo_system.getRandomCompetitors()
        movie_a, movie_b = competing_movies
        # Have the two movies compete
        winner = interface.choose_option(movie_name1=movie_a.name, movie_name2=movie_b.name)
        if winner in ['1', '2']:
            # Calculate the new elo of the two movies
            elo_system.recordMatch(movie_a.name, movie_b.name, winner=(competing_movies[int(winner)-1]).name)
        elif winner == 'q':
            break
        # Update the database
        movie_df = movie_writer.update_database(movie_df=movie_df, movie1=movie_a, movie2=movie_b)
        movie_writer.write_to_csv(dataframe=movie_df, file_name=path_to_database)
    # Repeat Loop 



if __name__ == "__main__":
    main()