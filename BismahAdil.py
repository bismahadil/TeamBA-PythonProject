def BismahAdil(): 
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Calculator Results")

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    if b == 0:
        division = "Error: Division by zero"
    else:
        division = a / b 
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
def main():
    BismahAdil()

if __name__ == "__main__":
    main()
