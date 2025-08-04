import math

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
        return "Cannot divide by zero!"

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)


history = []

print("====== Advanced Calculator with History ======")

while True:
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Show History")
    print("8. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

    if choice == '8':
        print("Calculator closed. Goodbye!")
        break

    elif choice == '7':
        print("\nCalculation History:")
        if history:
            for item in history:
                print(item)
        else:
            print("No calculations yet.")
        continue

    elif choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
            history.append(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
            history.append(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
            history.append(f"{num1} * {num2} = {result}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
            history.append(f"{num1} / {num2} = {result}")

        elif choice == '5':
            result = power(num1, num2)
            print(f"Result: {num1} ^ {num2} = {result}")
            history.append(f"{num1} ^ {num2} = {result}")

    elif choice == '6':
        num = float(input("Enter the number: "))
        result = square_root(num)
        print(f"Square root of {num} is {result}")
        history.append(f"√{num} = {result}")

    else:
        print("Invalid input. Please enter a valid option.")