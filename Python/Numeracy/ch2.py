# EX1 - Averages
def ex1():
    # Imports
    from statistics import mean, median, mode, multimode

    # Variables
    data = []

    # Input
    print('Enter your numbers one at a time.')
    print('When finished type "done"')

    while True:
        user_input = input("Please enter a number: ")
        if user_input == "done":
            break
        number = int(user_input)
        data.append(number)

    # Calculations
    data_mean = mean(data)
    data_median = median(data)
    data_mode = mode(data)
    data_mode_list = multimode(data)
    total = sum(data)
    smallest = min(data)
    largest = max(data)
    range = largest - smallest
    how_many = len(data)
    inorder = sorted(data)

    # Output
    print(f'The mean is {data_mean}')
    print(f'because the total is {total}')
    print(f'and this is divided by {how_many} (how many numbers).')
    print(f'The median is {data_median}')
    print('because the numbers in order are')
    print(inorder)
    print(f'and {data_median} is in the middle')
    print(f'The most common number is {data_mode_list}')
    print(f'if there is more than one mode the first one is {data_mode}')
    print(f'The range is {range}')
    print(f'because it is the largest {largest}')
    print(f'take away the smallest {smallest}')
 
# EX2 - Average Mean
def ex2():
    # Variables
    total = 0
    how_many = 0

    # Input
    print('Enter your numbers one at a time.')
    print('When finished type "done"')

    while True:
        user_input = input("Please enter a number: ")
        if user_input == "done":
            break
        number = float(user_input)
        total = total + number
        how_many += 1

    # Calculations
    data_mean = total / how_many

    # Output
    print(f'The mean is {data_mean}')
    print(f'because the total is {total}')
    print(f'and this is divided by {how_many} (how many numbers).')

# EX3 - Running Range
def ex3():
    # Variables
    print('Enter your numbers one at a time.')
    print('When finished type "done"')
    how_many = 1
    user_input = float(input("Please enter a number: "))
    total = largest = smallest = user_input

    # Input
    while True:
        user_input = input("Please enter a number or done: ")
        if user_input == "done":
            break
        number = float(user_input)
        total = total + number
        how_many += 1
        if number > largest:
            biggest = number
        if number < smallest:
            smallest = number

    # Calculations
    data_mean = total / how_many
    range = largest - smallest

    # Output
    print(f'The mean is {data_mean}')
    print(f'because the total is {total}')
    print(f'and this is divided by {how_many} (how many numbers).')
    print(f'The range is {range}')
    print(f'because it is the largest {largest}')
    print(f'take away the smallest {smallest}')

# EX4 - Fractions
def ex4():
    # Imports
    from random import randint

    # Variables
    marks = 0

    # Input
    q_num = int(input('How many fraction questions do you want? '))

    # Calculations
    for question in range(q_num):
        numerator = randint(1, 6)
        denominator = randint(numerator + 1, 9)
        whole = randint(2, 20) * denominator
        result = int(whole * (numerator / denominator))
        print(' ' + str(numerator))
        print('___ of', whole, '= ')
        print(' ' + str(denominator))
        answer = int(input('find the fraction of the amount above\n'))
        if answer == result:
            marks += 1
            print('Ka rawe, that is correct\n')
        else:
            print(f'sorry the answer was {result}')

    # Output
    percent = marks / q_num * 100
    print(f'You got {marks} correct, which is {percent}%')

option = int(input(f'PYTHON NUMERACY - CHAPTER 2\n1 - Averages\n2 - Average Mean\n3 - Running Range\n4 - Fractions\nSelect an option: '))

if option == 1: ex1()
elif option == 2: ex2()
elif option == 3: ex3()
elif option == 4: ex4()
else: 
    print('Please select an option 1-4!')
    exit(1)