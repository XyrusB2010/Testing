# Imports
import random

# Variables
die1 = [1, 1, 3, 5, 5, 6]
die2 = [2, 3, 3, 4, 4, 5]
die3 = [1, 2, 2, 4, 6, 6]
diceList = [die1, die2, die3]
p1score = 0
p2score = 0
winner = ''
winnerScore = 0

# Welcome Message
print(f"""Welcome to 'My rock paper scissors dice game'.
The program will ask how many times to randomly roll two dice.
Then two players enter their names and the first player picks a die.
The second player picks one of the remaining dice.
The program will print out each roll and who wins each time or if it is a draw.
If one player has more wins, they will be declared the winner.
Be polite, manners are important!
      
The dice to choose from are:
Die 1: {die1}
Die 2: {die2}
Die 3: {die3}""")

# Functions
def getRolls():
    try:
        rolls = int(input('How many rolls in the game? '))
        if rolls < 1:
            print('Error: Please enter a number greater than 0 for rolls.')
            getRolls()
    except ValueError:
        print('Error: Please enter a valid number greater than 0 for rolls.')
        getRolls()
    return rolls

def getNames():
    player1 = input("Enter player one's name please: ").title().strip()
    player2 = input("Enter player two's name please: ").title().strip()
    if not player1 or not player2:
        print('Error: Player names cannot be empty.')
        getNames()
    if player1 == player2:
        print('Both players have the same name, please enter different names for the players.')
        getNames()
    return player1, player2

def getDice():
    try:
        player1die = int(input(f"{player1}, which die do you want? 1, 2 or 3: "))
        player2die = int(input(f"{player2}, which die do you want from the two remaining? "))
        if player1die not in [1, 2, 3] or player2die not in [1, 2, 3]:
            print('Error: Please enter a valid number for the die choice (1, 2 or 3).')
            getDice()
        elif player1die == player2die:
            print('Error: Both players cannot choose the same die. Please choose different dice.')
            getDice()
    except ValueError:
        print('Error: Please enter a valid number for the die choice.')
        getDice()
    return diceList[player1die - 1], diceList[player2die - 1]

while True:
    # Inputs
    rolls = getRolls()
    player1, player2 = getNames()
    player1die, player2die = getDice()

    # Game
    for i in range(rolls):
        player1roll = random.choice(player1die)
        player2roll = random.choice(player2die)

        if player1roll > player2roll:
            p1score += 1
            print(f"{player1roll} vs {player2roll}. Score is {p1score} to {p2score}, this time {player1} wins")
        elif player2roll > player1roll:
            p2score += 1
            print(f"{player1roll} vs {player2roll}. Score is {p1score} to {p2score}, this time {player2} wins")
        else:
            print(f"{player1roll} vs {player2roll}. Score is {p1score} to {p2score}, this time it is a draw")

    # Results
    print(f'{player1} got {p1score}')
    print(f'{player2} got {p2score}')
    if p1score > p2score:
        winner = player1
        winnerScore = p1score
    elif p2score > p1score:
        winner = player2
        winnerScore = p2score
    percent = round(winnerScore / (p1score + p2score) * 100, 2)
    print(f'{winner} wins with {percent}% of the wins')
    if percent > 54:
        print('Massive win!')
    elif percent > 52:
        print('Good win.')
    else:
        print('Close.')
    if not input('Play again? (y/N): ').strip().lower().startswith('y'):
        print('Thanks for playing!')
        break