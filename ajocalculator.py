
import math

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numerical values.")
        return None, None

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero."

def square(num):
    return num ** 2

def square_root(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return "Error: Cannot calculate square root of a negative number."

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square Root")

    choice = input("Enter the operation number (1-6): ")

    num1, num2 = get_user_input()

    if num1 is None or num2 is None:
        return

    if choice == '1':
        result = addition(num1, num2)
    elif choice == '2':
        result = subtraction(num1, num2)
    elif choice == '3':
        result = multiplication(num1, num2)
    elif choice == '4':
        result = division(num1, num2)
    elif choice == '5':
        result = square(num1)
    elif choice == '6':
        result = square_root(num1)
    else:
        print("Error: Invalid operation number.")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
