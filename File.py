def Bismah(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Invalid operator"

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

result = Bismah(a, operator, b)
print("Result:", result)
