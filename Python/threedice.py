# Imports
import random

# Variables
die1 = [1, 1, 3, 5, 5, 6]
die2 = [2, 3, 3, 4, 4, 5]
die3 = [1, 2, 2, 4, 6, 6]
p1score = 0
p2score = 0
winner = ''
winnerScore = 0

# Welcome Message
print("Welcome to 'My rock paper scissors dice game'.")
print('The program will ask how many times to randomly roll two dice.')
print('Then two players enter their names and the first player picks a die.')
print('The second player picks one of the remaining dice.')
print('The program will print out each roll and who wins each time or if it is a draw.')
print('If one player has more wins, they will be declared the winner.')
print('Be polite, manners are important!')
print()
print('The dice to choose from are:')
print(f'Die 1: {die1}')
print(f'Die 2: {die2}')
print(f'Die 3: {die3}')

# Input
rolls = int(input('How many rolls in the game? '))
player1 = input("Enter player one's name please: ")
player2 = input("Enter player two's name please: ")
player1die = int(input(f"{player1}, which die do you want? 1, 2 or 3: "))
player2die = int(input(f"{player2}, which die do you want from the two remaining? "))

# Game
for i in range(rolls):
    if player1die == 1:
        p1roll = random.choice(die1)
    elif player1die == 2:
        p1roll = random.choice(die2)
    else:
        p1roll = random.choice(die3)

    if player2die == 1:
        p2roll = random.choice(die1)
    elif player2die == 2:
        p2roll = random.choice(die2)
    else:
        p2roll = random.choice(die3)
    
    if p1roll > p2roll:
        p1score += 1
        print(f"{p1roll} vs {p2roll}. Score is {p1score} to {p2score}, this time {player1} wins")
    elif p2roll > p1roll:
        p2score += 1
        print(f"{p1roll} vs {p2roll}. Score is {p1score} to {p2score}, this time {player2} wins")
    else:
        print(f"{p1roll} vs {p2roll}. Score is {p1score} to {p2score}, this time it is a draw")

# Results
print(f'{player1} got {p1score}')
print(f'{player2} got {p2score}')
if p1score > p2score:
    winner = player1
    winnerScore = p1score
elif p2score > p1score:
    winner = player2
    winnerScore = p2score
percent = winnerScore / (p1score + p2score) * 100
print(f'{winner} wins with {percent}% of the wins')
if percent > 54:
    print('Massive win!')
elif percent > 52:
    print('Good win.')
else:
    print('Close.')