import random

def is_valid_number(number):
    return number.isdigit() and 0 <= int(number) <= 999

def format_number(number):
    return f"{int(number):03}"

def play_game():
    print("\nWelcome to the Fermi, Pico, Bagels Game!")
    print("Rules:")
    print("- The computer or the first player will choose a number between 000 and 999.")
    print("- The second player (or you in solo mode) has to guess the number.")
    print("- Feedback will be given for each guess:")
    print("  * 'Fermi' means a correct digit in the correct position.")
    print("  * 'Pico' means a correct digit in the wrong position.")
    print("  * 'Bagels' means no correct digits.\n")

    type_of_game = input("Wanna play: \n1- Solo(1) \n2- Duo(2) \n-> ")

    if type_of_game == "2":
        while True:
            number = input("Enter a number between 0 and 999: ")
            if not is_valid_number(number):
                print("Invalid number, try again.")
                continue
            number = format_number(number)
            break

        while True:
            guess = input("The second player should guess the number: ")
            if not is_valid_number(guess):
                print("Invalid guess, try again.")
                continue
            guess = format_number(guess)

            if guess == number:
                print("Nice guess, that's true")
                break

            found = False
            matched_positions = [False] * 3

            for i in range(3):
                if guess[i] == number[i]:
                    print("Fermi")
                    matched_positions[i] = True
                    found = True

            for i in range(3):
                if not matched_positions[i] and guess[i] in number:
                    if number.count(guess[i]) > guess[:i].count(guess[i]):
                        print("Pico")
                        found = True

            if not found:
                print("Bagels")
            print("Try again.")

    elif type_of_game == "1":
        number = format_number(str(random.randint(0, 999)))
        while True:
            guess = input("Guess the number: ")
            if not is_valid_number(guess):
                print("Invalid guess, try again.")
                continue
            guess = format_number(guess)

            if guess == number:
                print("Nice guess, that's true")
                break

            found = False
            matched_positions = [False] * 3

            for i in range(3):
                if guess[i] == number[i]:
                    print("Fermi")
                    matched_positions[i] = True
                    found = True

            for i in range(3):
                if not matched_positions[i] and guess[i] in number:
                    if number.count(guess[i]) > guess[:i].count(guess[i]):
                        print("Pico")
                        found = True

            if not found:
                print("Bagels")
            print("Try again.")

    else:
        print("Invalid option. Please select 1 or 2.")

while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'n':
        print("Thank you for playing! Goodbye!")
        break