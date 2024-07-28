def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Welcome to the Simple Calculator!")

    try:
        # Get user input
        num1 = float(input("Enter the number1: "))
        num2 = float(input("Enter the number2: "))

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter the number of the operation (1/2/3/4): ")

        if choice == '1':
            print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("Invalid input! Please choose a valid operation.")

    except ValueError:
        print("Invalid input! Please enter numeric values for the numbers.")

if __name__ == "__main__":
    main()