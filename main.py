import art

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

operations = {
    "+" : addition,
    "-" : subtraction,
    "x" : multiplication,
    "/" : division
    }

print(art.logo)
calculation = input("Write the calculation you want to make: ")
calculation_list = calculation.split()