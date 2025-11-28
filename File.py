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


import random

def amnamirzagame():   
    print("<<Welcome to the Guessing Game>>")

    while True:
        number = random.randint(1, 50)
        attempts = 0

        print(" Guess a number between 1 and 50.")

        guess = 0
        while guess != number:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Your guess is too low!")
            elif guess > number:
                print(" your guess is too high!")
        
        print("You guessed it! Congratulations")
        print("Total attempt(s):", attempts)

        again_playing = input(" Do you want to Play again? (yes/no): ")
        if again_playing.lower() != "yes":
            print("Thank you for playing.Looking forward to seeing you in the next level")
            break


amnamirzagame()
