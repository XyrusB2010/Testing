# EX1 - Rounding
def ex1():
    # Input
    problem = int(input('Enter a number between 100 and 9,999: '))

    # Calculations
    answer10 = round(problem, -1)
    answer100 = round(problem,-2)
    answer1000 = round(problem, -3)

    # Output
    print(f'{problem} rounded to nearest ten is {answer10}')
    print(f'{problem} rounded to nearest hundred is {answer100}')
    print(f'{problem} rounded to nearest thousand is {answer1000}')

# EX2 - Integers
def ex2():
    # Input
    integer1 = int(input('Enter the first integer: '))
    integer2 = int(input('Enter the second integer: '))

    # Calculations
    bigger = integer1 > integer2
    equal = integer1 == integer2
    smaller = integer1 < integer2
    minus = integer1 - integer2
    plus = integer1 + integer2

    # Output
    print(f'The statement that {integer1} is greater than {integer2} is {bigger}')
    print(f'The statement that {integer1} is less than {integer2} is {smaller}')
    print(f'The statement that {integer1} is equal to {integer2} is {equal}')
    print(f'{integer1} + {integer2} = {plus}')
    print(f'{integer1} - {integer2} = {minus}')

# EX3 - Powers
def ex3():
    # Input
    base = input('Enter the base number: ')
    power = input('Enter the power (exponent or index): ')

    # Calculations
    expanded = base + ((" x " + base) * (int(power) - 1))
    answer = int(base) ** int(power)

    # Output
    print(f'The number {base} to the power of {power} is ')
    print(f'{expanded} expanded out')
    print(f'and it equals {answer}')

# EX4 - Words
def ex4():
    # Input
    choc_cost = float(input('How much is the box of chocolates: '))
    card_cost = float(input('How much is the card: '))
    number = int(input('How many students in the class: '))

    # Calculations
    answer = (choc_cost + card_cost) / number

    # Output
    print(f'The cost per student is ${answer:.2f} ')

# EX5 - Ratios
def ex5():
    # Input
    money = float(input('How much money: '))
    part1 = int(input('First part: '))
    part2 = int(input('Second part: '))

    # Calculations
    total_parts = part1 + part2
    share1 = (money / total_parts) * part1
    share2 = (money / total_parts) * part2

    # Output
    print(f'The money for the first part is ${share1:.2f} ')
    print(f'The money for the Second part is ${share2:.2f} ')

option = int(input(f'PYTHON NUMERACY - CHAPTER 1\n1 - Rounding\n2 - Integers\n3 - Powers\n4 - Words\n5 - Ratios\nSelect an option: '))

if option == 1: ex1()
elif option == 2: ex2()
elif option == 3: ex3()
elif option == 4: ex4()
elif option == 5: ex5()
else: 
    print('Please select an option 1-5!')
    exit(1)