from Calculator_Art import logo

def add(num1, num2):
    result = num1 + num2
    return result

def substract(num1, num2):
    result = num1 - num2
    return result

def multiple(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    if num1 == 0:
        print(f"It is wrong. {num1} can't be divided.")
    else:
        result = num1 / num2
        return result

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiple,
    "/" : divide,
}

def calculate():
    print(logo)
    number_1 = input("What is the first number? : ")
    if "." in number_1:
        number_1 = float(number_1)
    else:
        number_1 = int(number_1)

    for operator in operations:
        print(operator)
    isContinued = True

    while isContinued:
        operation_option = input("Pick an operation: ")
        number_2 = input("What is the second number? : ")
        if "." in number_2:
            number_2 = float(number_2)
        else:
            number_2 = int(number_2)
        calculating = operations[operation_option]
        result = calculating(number_1,number_2)
        print(f"{number_1} {operation_option} {number_2} = {result}")

        calculating_answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit. : ")

        if calculating_answer == 'n':
            calculate()
        elif calculating_answer == 'y':
            number_1 = result
        else:
            print("It is fault input text. Please try again to first!")
            isContinued = False
            break

calculate()