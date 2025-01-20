from movie import Movie
from rankingalgorithm import RankingSystem
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
    new_movie_df = movie_writer.generate_new_movie_dataframe(list_of_new_movies=new_movies_list)
    movie_writer.write_to_csv(dataframe=new_movie_df, file_name=path_to_database)

    # Begin loop
    # Draw two movies from the database, prioritizing ones with fewer competitions
    # Have the two movies compete
    # Calculate the new elo of the two movies
    # Update the database
    # Repeat Loop 



if __name__ == "__main__":
    main()