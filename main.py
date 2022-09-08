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

if len(calculation_list) == 3:
    first_number = int(calculation_list[0])
    second_number = int(calculation_list[2])
    symbol = calculation_list[1]
    if symbol in operations:
        calculation_operation = operations[symbol]
        result = calculation_operation(first_number, second_number)
        print(result)