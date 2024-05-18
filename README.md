# Number_Guess_Quiz_PYTHON
    Input Validation:
        The script prompts the user to input a number, which represents the upper range for the random number to be generated.
        It checks if the input is a valid positive integer. If not, appropriate error messages are displayed, and the script quits.

    Generating a Random Number:
        The script generates a random number between 0 and the specified upper range using the random.randint() function.

    Guessing Loop:
        The script enters a loop where the user repeatedly guesses the random number.
        Each time the user makes a guess, the number of guesses is incremented.
        The script checks if the user's guess matches the random number. If it does, the script congratulates the user and breaks out of the loop.
        If the guess is incorrect, the script informs the user and continues the loop.

    Input Validation for Guesses:
        Inside the loop, the script validates the user's input to ensure it's a valid integer. If not, appropriate error messages are displayed, and the loop continues.

    End of Game:
        Once the user guesses the correct number, the script prints the total number of guesses made by the user.
