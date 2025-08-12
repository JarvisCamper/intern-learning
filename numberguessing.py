import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))
        if guess < number_to_guess:
            print("Too low, try again!")
        elif guess > number_to_guess:
            print("Too high, try again!")
        else:
            print("Congratulations! You have guessed the correct number.")
            break
    except ValueError:
        print("Please enter a valid number!")
 