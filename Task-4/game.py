import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    print("\n--- Rock Paper Scissors ---")
    user = input("Enter rock, paper, scissors or quit: ").lower()

    if user == "quit":
        print("Game Over")
        print("Final Score → You:", user_score, "Computer:", computer_score)
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Score → You:", user_score, "| Computer:", computer_score)