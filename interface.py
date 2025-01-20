import keyboard
class Interface:
    def choose_option(self, movie_name1, movie_name2):
        """
        Displays two options to the user, captures the choice (1 or 2) without requiring Enter,
        and logs the selection.
        """
        option1 = movie_name1
        option2 = movie_name2

        print(f"Option 1: {option1}")
        print(f"Option 2: {option2}")
        user_input = input("\nPress '1' for Option 1 or '2' for Option 2.\n")

        return user_input
