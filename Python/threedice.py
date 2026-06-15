# Imports
import random

# Variables
die1 = [1, 1, 3, 5, 5, 6]
die2 = [2, 3, 3, 4, 4, 5]
die3 = [1, 2, 2, 4, 6, 6]
diceList = [die1, die2, die3]
p1Name = ''
p2Name = ''
p1Die = 0
p2Die = 0
p1Roll = 0
p2Roll = 0
p1Score = 0
p2Score = 0
winner = ''
winnerScore = 0

welcomeMsg = f'''
Welcome to 'My rock paper scissors dice game'.
The program will ask how many times to randomly roll two dice.
Then two players enter their names and the first player picks a die.
The second player picks one of the remaining dice.
The program will print out each roll and who wins each time or if it is a draw.
If one player has more wins, they will be declared the winner.
Be polite, manners are important!

The default dice to choose from are:
Die 1: {die1}
Die 2: {die2}
Die 3: {die3}
'''

# Functions
def menu():
    while True:
        print('''
Welcome to 'My rock paper scissors dice game'.

Main Menu
1. Play Game
2. Help
3. Configure dice
4. Exit
''')
        choice = input('Enter your choice (1, 2, 3 or 4): ').strip()
        if choice == '1':
            main()
        elif choice == '2':
            print(welcomeMsg)
            continue
        elif choice == '3':
            configureDice()
        elif choice == '4':
            print('Thanks for playing!')
            exit()
        else:
            print('Invalid choice. Please enter 1 to play, 2 to view the help message, or 3 to configure custom dice, or 4 to exit.')

def configureDice():
    while True:
        print(f'\nEnter a configuration for a new dice. Each die should have 6 numbers between 1 and 6.')
        try:
            dieConfig = input('Enter the configuration for the new dice: ').strip()
            if not dieConfig:
                print('Error: Die configuration cannot be empty.')
                continue
            dieNumbers = [int(x) for x in list(dieConfig.strip())]
            if len(dieNumbers) != 6:
                print('Error: Please enter exactly 6 numbers for the die configuration.')
                continue
            if not all(1 <= x <= 6 for x in dieNumbers):
                print('Error: Each number in the die configuration must be between 1 and 6.')
                continue
            diceList.append(dieNumbers)
            print('New dice configured successfully!')
            break
        except ValueError:
            print('Error: Please enter valid numbers for the die configuration.')
            continue

def getRolls():
    while True:
        try:
            rolls = int(input('How many rolls in the game? '))
            if rolls < 1:
                print('Error: Please enter a number greater than 0 for rolls.')
                continue
        except ValueError:
            print('Error: Please enter a valid number greater than 0 for rolls.')
            continue
        return rolls

def getNames():
    while True:
        p1Name = input("Enter player one's name please: ").title().strip()
        p2Name = input("Enter player two's name please: ").title().strip()
        if not p1Name or not p2Name:
            print('Error: Player names cannot be empty.')
            continue
        if p1Name == p2Name:
            print('Both players have the same name, please enter different names for the players.')
            continue
        return p1Name, p2Name

def getDice(p1Name, p2Name):
    while True:
        try:
            p1Die = int(input(f"{p1Name}, which die do you want? {', '.join(str(i) for i in range(1, len(diceList) + 1))}: "))
            if p1Die not in range(1, len(diceList) + 1):
                print('Error: Please enter a valid number for the die choice.')
                continue
            p2Die = int(input(f"{p2Name}, which of the remaining die do you want? {', '.join(str(i) for i in range(1, len(diceList) + 1) if i != p1Die)}: "))
            if p2Die not in range(1, len(diceList) + 1):
                print('Error: Please enter a valid number for the die choice.')
                continue
            if p1Die == p2Die:
                print('Error: Both players cannot choose the same die. Please choose different dice.')
                continue
        except ValueError:
            print('Error: Please enter a valid number for the die choice.')
            continue
        return diceList[p1Die - 1], diceList[p2Die - 1]

def main():
    while True:
        # Dice Options
        print(f'\nThe dice to choose from are:')
        for i, die in enumerate(diceList, start=1):
            print(f'Die {i}: {die}')
        print()

        # Inputs
        rolls = getRolls()
        p1Name, p2Name = getNames()
        p1Die, p2Die = getDice(p1Name, p2Name)
        p1Score = 0
        p2Score = 0
        
        print()

        # Game
        for i in range(rolls):
            p1Roll = random.choice(p1Die)
            p2Roll = random.choice(p2Die)

            if p1Roll > p2Roll:
                p1Score += 1
                print(f"{p1Roll} vs {p2Roll}. Score is {p1Score} to {p2Score}, this time {p1Name} wins")
            elif p2Roll > p1Roll:
                p2Score += 1
                print(f"{p1Roll} vs {p2Roll}. Score is {p1Score} to {p2Score}, this time {p2Name} wins")
            else:
                print(f"{p1Roll} vs {p2Roll}. Score is {p1Score} to {p2Score}, this time it is a draw")

        # Results
        print(f'\n{p1Name} got {p1Score}')
        print(f'{p2Name} got {p2Score}\n')
        if p1Score > p2Score:
            winner = p1Name
            winnerScore = p1Score
        elif p2Score > p1Score:
            winner = p2Name
            winnerScore = p2Score
        else:
            winner = None
        totalWins = p1Score + p2Score
        if winner:
            percent = round((winnerScore / totalWins) * 100, 2) if totalWins else 0
            print(f'{winner} wins with {percent}% of the wins.')
        else:
            percent = 0
            print('The game is a draw with no winner.')
        if percent > 54:
            print('Massive win!')
        elif percent > 52:
            print('Good win.')
        else:
            print('Close.')
        if not input(f'\nPlay again? (y/N): ').strip().lower().startswith('y'):
            return

# Start Program
menu()