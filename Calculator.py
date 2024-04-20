print("*** Hello CognoRise ***")

print("       {{Task 1}}      ")

print("----------------------------------- \n Welcome to Calculator... \n -----------------------------------")

print("Arithmetic Operations:")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

while True:
    choice = input("Enter choice (A/B/C/D): ")

    if choice in ('A', 'B', 'C', 'D'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'A':
            print("Result:", add(num1, num2))
        elif choice == 'B':
            print("Result:", subtract(num1, num2))
        elif choice == 'C':
            print("Result:", multiply(num1, num2))
        elif choice == 'D':
            print("Result:", divide(num1, num2))
    else:
        print("Please enter a valid input (These values are case sensitive)")

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        break
