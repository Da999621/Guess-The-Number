import random

secret_number = random.randint(1, 100)   # Generate a random number between 1 and 100

max_attempts = 5    # Set the maximum number of attempts

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

# Loop for user attempts
for attempt in range(max_attempts):
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!\n")
    elif guess > secret_number:
        print("Too high!\n")
    else:
        print("Congratulations! You guessed the number correctly!")
        break
else:
    print(f"Sorry! You've used all attempts. The number was {secret_number}.")
