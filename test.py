# generic_script.py

def greetuser(name):
    return f"Hello, {name}! Welcome to this Python script."

def addnumbers(a, b):
    return a + b

def main():
    print("Generic Python Script")
    name = input("Enter your name: ")
    print(greetuser(name))

    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = addnumbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
