import random

# Generate a random number between 1 and 100
x = random.randint(1, 100)

# Prompt the user for input
y = int(input("Enter a number between 1 and 100: "))

# Loop until the user guesses the correct number
while y != x:
    if y < x:
        print("Too low")
    elif y > x:
        print("Too high")
    
    # Ask the user to try again
    y = int(input("Enter a number between 1 and 100: "))

# When the loop exits, the guess is correct
print("You guessed it!")
print("The correct number is:", x)
