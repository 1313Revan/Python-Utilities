# A calculator I made in the very early days of learning Python, the original variation
# Author: Revan

def prompt_menu():
    # User Input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("""
    Choose an operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exponent
    6. Division with Remainder
    """)

    op = int(input("Enter choice: "))
    return num1, num2, op


def calculate():
    # Perform Operations
    num1, num2, op = prompt_menu()
    if op == 1:
        print("Sum: {} + {} = {}".format(num1,num2,num1+num2))
    elif op == 2:
        print("Difference: {} - {} = {}".format(num1,num2,num1-num2))
    elif op == 3:
        print("Product: {} * {} = {}".format(num1,num2,num1*num2))
    elif op == 4:
        try:
            print("Quotient: {} / {} = {}".format(num1,num2,num1/num2))
        except:
            print("Division by 0 not possible.")
    elif op == 5:
        print("Power: {} ** {} = {}".format(num1,num2,num1**num2))
    elif op == 6:
        try:
            print("Quotient: {} / {} = {}, Remainder: {}".format(num1,num2,num1/num2,num1%num2))
        except:
            print("Division by 0 not possible.")
    else:
        print("Please choose a valid option")
    loop()


def loop():
    choice = input("Do you wish to continue? (Y/N): ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("Goodbye!")
        exit()
    else:
        print("Please choose a valid option.")
        loop()


calculate()
