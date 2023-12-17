import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
guesses_taken = 0
guessed_correctly = False

# Loop until the user guesses correctly or runs out of guesses
while guesses_taken < 5 and not guessed_correctly:
  guess = int(input("Guess the number between 1 and 100: "))
  guesses_taken += 1

  if guess == secret_number:
    guessed_correctly = True
    print("You guessed it! The number was", secret_number, "and it took you", guesses_taken, "guesses.")
  elif guess < secret_number:
    print("Too low! Try again.")
  else:
    print("Too high! Try again.")

if not guessed_correctly:
  print("Sorry, you ran out of guesses. The number was", secret_number)

