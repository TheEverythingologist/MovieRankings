import keyboard
class Interface:
    def choose_option(movie_name1, movie_name2):
        """
        Displays two options to the user, captures the choice (1 or 2) without requiring Enter,
        and logs the selection.
        """
        option1 = movie_name1
        option2 = movie_name2

        print(f"Option 1: {option1}")
        print(f"Option 2: {option2}")
        print("\nPress '1' for Option 1 or '2' for Option 2.")

        choice = None

        while choice not in ['1', '2']:
            # Wait for a key press (non-blocking)
            if keyboard.is_pressed('1'):
                choice = '1'
            elif keyboard.is_pressed('2'):
                choice = '2'

        return choice