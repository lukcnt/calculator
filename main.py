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
user_arithmetic_calculation = input("Write the calculation you want to make: ")
calculation_list = user_arithmetic_calculation.split()
result = calculation(calculation_list)
print(result)