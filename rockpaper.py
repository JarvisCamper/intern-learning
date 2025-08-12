import random

choices = ('r', 'p', 's')
choice_names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        return "You win!"
    else:
        return "Computer wins!"

user_wins = 0
computer_wins = 0
ties = 0
games_played = 0

while True:
    user_choice = input('\nRock, Paper or Scissors? (r/p/s): ').lower()
    
    if user_choice not in choices:
        print('Invalid input choice')
        continue
    
    computer_choice = random.choice(choices)
    games_played += 1
    
    print(f'You choose {choice_names[user_choice]}')
    print(f'Computer choose {choice_names[computer_choice]}')
    result = determine_winner(user_choice, computer_choice)
    print(result)
 
    if result == "You win!":
        user_wins += 1
    elif result == "Computer wins!":
        computer_wins += 1
    else:
        ties += 1
   
    print(f'\nStats: Games={games_played}, User Wins={user_wins}, Computer Wins={computer_wins}, Ties={ties}')
    
    play_again = input('\nDo you want to play again? (y/n): ').lower()
    if play_again != 'y':
        print('Thanks for playing!')
        print(f'Final Stats: Games={games_played}, User Wins={user_wins}, Computer Wins={computer_wins}, Ties={ties}')
        break
