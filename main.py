import art
import os

INITIAL_MESSAGE = ("Welcome to the python calculator, to work properly is needed "
                  "typing spaces between numbers and operator. Example: 20 + 15\n"
                  "For more information type 'help'.")

HELP_MESSAGE = ("\nThe only operations supported at the moment are the following:\n"
                "-Addition using the symbol '+'\n"
                "-Subtraction using the symbol '-'\n"
                "-Multiplication using the letter 'x'\n"
                "-Division using the symbol '/'\n"
                "\nLastly, if you want to clean the screen write 'clean'")

def addition(first_number, second_number):
    sum = first_number + second_number
    return sum

def subtraction(first_number, second_number):
    difference = first_number - second_number
    return difference

def multiplication(first_number, second_number):
    product = first_number * second_number
    return product

def division(first_number, second_number):
    quotient = first_number / second_number
    return quotient

def calculation(calculation_list):
    first_number = int(calculation_list[0])
    second_number = int(calculation_list[2])
    symbol = calculation_list[1]
    if symbol in operations:
        calculation_operation = operations[symbol]
        result = calculation_operation(first_number, second_number)
    return result

operations = {
    "+" : addition,
    "-" : subtraction,
    "x" : multiplication,
    "/" : division
    }

print(art.logo)
print(INITIAL_MESSAGE)
keep_running_program = True
while keep_running_program == True:
    user_arithmetic_calculation = input("Write the calculation you want to make: ")
    if user_arithmetic_calculation == "exit":
        keep_running_program = False
    elif user_arithmetic_calculation == "clear":
        os.system("clear")
        print(art.logo)
        print(INITIAL_MESSAGE)
    elif user_arithmetic_calculation == "help":
        print(HELP_MESSAGE)
    else:
        calculation_list = user_arithmetic_calculation.split()
        result = calculation(calculation_list)
        print(f"The result is: {result}")