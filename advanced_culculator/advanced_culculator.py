import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x ** y

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def log(x, base):
    return math.log(x, base)

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Sin")
    print("7. Cos")
    print("8. Tan")
    print("9. Log")

    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**", num2, "=", exponent(num1, num2))

    elif choice in ('6', '7', '8', '9'):
        num = float(input("Enter number: "))

        if choice == '6':
            print("sin", num, "=", sin(num))

        elif choice == '7':
            print("cos", num, "=", cos(num))

        elif choice == '8':
            print("tan", num, "=", tan(num))

        elif choice == '9':
            base = float(input("Enter base for logarithm: "))
            print("log", num, "base", base, "=", log(num, base))

    else:
        print("Invalid input")

if __name__ == "__main__":
    main()