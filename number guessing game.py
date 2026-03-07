import random

def layout_of_game():
    minimum = 1
    maximum = 100
    number_of_guesses_left = 5
   
   
 
    secret_random_generated_number = random.randint(minimum, maximum)
    print(f"I'm thinking of a number between {minimum} and {maximum}.")
    print("You have 5 guesses")
   
    while number_of_guesses_left > 0:
        guess_by_user = input("Take a guess: ")

        if not guess_by_user.isdigit():
            print("Invalid number! Please enter a number between 1 and 100 to continue:\n")
            continue

        guess_by_user = int(guess_by_user)

        if guess_by_user < minimum or guess_by_user > maximum:
            print("Invalid number! Please enter a number between 1 and 100 to continue:\n")
            continue
       
        if guess_by_user > secret_random_generated_number:
            print("Lower!")
        elif guess_by_user < secret_random_generated_number:
            print("Higher!")
        else:
            print("Correct!")
            return  
       
        number_of_guesses_left -= 1
        print(f"Guesses remaining: {number_of_guesses_left}\n")
   
    print(f"Out of guesses! The number was {secret_random_generated_number}.")




def play_number_guessing_game():
    while True:
        layout_of_game()
       
        play_game_again = input("Play again? (yes/no): ").lower()
        if play_game_again == "no":
            print("Thanks for playing!")
            break
        elif play_game_again == "yes":
            continue
        else:
            print("Invalid input. Please enter a valid input (yes or no")


print("Welcome to the Number Guessing Game!")
play_number_guessing_game()

