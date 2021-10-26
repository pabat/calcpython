def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
* for multiplication
/ for division
+ for addition
- for subtraction

''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))



    print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()