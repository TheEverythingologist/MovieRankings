class Reader:
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
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()  # Remove leading/trailing whitespace
                    if line:  # Skip empty lines
                        try:
                            # Extract the name and year using rstrip and split
                            name, year = line.rsplit(' (', 1)
                            year = year.rstrip(')')  # Remove the closing parenthesis
                            result.append((name.strip(), int(year)))
                        except ValueError:
                            print(f"Skipping malformed line: {line}")
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
        return result
