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
        return "cannot divide by zero!"

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

print('======== Simple Calculator ========')

while True:
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Exit")
    
    choice = input('Enter your choice (1,2,3,4,5,6,7): ')
    
    if choice == '7':
        print("calculator closed. goodbye!")
        break
    
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        
        if choice == '1':
            print(f'Result: {num1} + {num2} = {add(num1, num2)}')
        elif choice == '2':
            print(f'Result: {num1} - {num2} = {subtract(num1, num2)}')
        elif choice == '3':
            print(f'Result: {num1} * {num2} = {multiply(num1, num2)}')
        elif choice == '4':
            print(f'Result: {num1} / {num2} = {divide(num1, num2)}')
        elif choice == '5':
            print(f'Result: {num1} ^ {num2} = {power(num1, num2)}')
    
    elif choice == '6':
        num = float(input('Enter the number: '))
        print(f'square root of {num} is {square_root(num)}')
        
    else:
        print('Invalid input. Please enter a valid option.')