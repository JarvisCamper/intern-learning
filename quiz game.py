import random

player_scores = {}

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 5 + 7?", "12"),
    ("What is the color of the sky?", "blue"),
    ("Who wrote 'Hamlet'?", "William shakespeare"),
    ("What is the largest planet in our Solar System?", "jupiter")
    
]

def quiz_game():
    name = input("Enter your name: ").strip().lower()
    
    
    if name not in player_scores:
        player_scores[name] = 0

    while True:
        score = 0
       
        random.shuffle(questions)
        
        for question, answer in questions:
            user_answer = input(question + " ").strip().lower()
            if user_answer == answer:
                print("Correct ✅")
                score += 1
            else:
                print(f"Wrong ❌ The correct answer was: {answer}")

        player_scores[name] += score
        print(f"{name}, your total score so far: {player_scores[name]}")

        
        cont = input("Do you want to play again? (yes/no): ").strip().lower()
        if cont != "yes":
            print(f"Thanks for playing, {name}! Your final score: {player_scores[name]}")
            break


quiz_game()
