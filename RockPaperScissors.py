import random

turns = 3
computerScore = 0
playerScore = 0

def turn():
    global computerScore, playerScore

    userChoice = input("Rock, paper, or scissors? ").lower()

    moveOptions = ['rock', 'paper', 'scissors']

    while (userChoice not in moveOptions):
        userChoice = input("Invalid choice. Must be rock, paper, or scissors: ").lower()

    print("")
    print(f"You chose {userChoice}.")

    computerChoice = random.choice(moveOptions)
    print(f"The computer chose {computerChoice}.")

    moves = {
    'rock': { 'beats': 'scissors', 'losesTo': 'paper' },
    'scissors': { 'beats': 'paper', 'losesTo': 'rock' },
    'paper': { 'beats': 'rock', 'losesTo': 'scissors' },
    }

    if userChoice == computerChoice:
        print(f"Both you and the computer chose {userChoice}. It's a tie!")
    else:
        if (moves[userChoice]['beats'] == computerChoice):
            print(f"{userChoice} beats {computerChoice}. You win this round!")
            playerScore += 1

        if (moves[userChoice]['losesTo'] == computerChoice):
            print(f"{userChoice} loses to {computerChoice}. The computer wins!")
            computerScore += 1

    # Print an update on the total scores after the round
    print("")
    print(f"SCOREBOARD | Player's score: {playerScore} | Computer's score: {computerScore}")

for i in range(turns):
    print("")
    print(f"--- Round {i+1}: ---")
    turn()

print("")

if (computerScore > playerScore):
    print(f"The computer wins with {computerScore} points!")
elif (playerScore > computerScore):
    print(f"You win with {playerScore} points!")
else:
    print(f"It's a tie! You both win with {playerScore} points!")

