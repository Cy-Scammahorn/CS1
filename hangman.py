import random

while True:

    words = ["fortnite", "valorant", "marvel rivals", "rainbow six siege", "overwatch", "grand theft auto V", "minecraft", "call of duty", "dead by daylight", "rocket league", "sea of thieves", "apex legends"]
    secret_word_used_for_hangman = random.choice(words)
    guessed_letters_by_user = []
    wrong_guesses = 0

    hangman_stages_until_death = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
    ]

    print("Welcome to Hangman!")

    while wrong_guesses < 6:

        print(hangman_stages_until_death[wrong_guesses])

        display_word_progress = ""

        for letter in secret_word_used_for_hangman:
            if letter == " ":
                display_word_progress += "  "
            elif letter in guessed_letters_by_user:
                display_word_progress += letter + " "
            else:
                display_word_progress += "_ "

        print("Word:", display_word_progress)

        if "_" not in display_word_progress:
            print("You win!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) > 1:
            if guess == secret_word_used_for_hangman.lower():
                print("You got it!")
                print("The word was:", secret_word_used_for_hangman)
                break
            else:
                wrong_guesses += 1
                print("Wrong word guess!")
                continue

        if guess in guessed_letters_by_user:
            print("You already guessed that letter.")
            continue

        guessed_letters_by_user.append(guess)

        if guess not in secret_word_used_for_hangman:
            wrong_guesses += 1
            print("Wrong guess!")

    if wrong_guesses == 6:
        print(hangman_stages_until_death[6])
        print("You lost! The word was:", secret_word_used_for_hangman)

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
