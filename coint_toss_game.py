# Steps (for simplifying the code logic):
# Step 1: Print a welcoming message to the player.
# Step 2: Initialize variables to keep track of the number of correct guesses and the total number of guesses.
# Step 3: Use a while loop to keep the game running until the player decides to quit.
# Step 4: If the player enters 'quit', exit the game loop.
# Step 5: Ask the player to guess the outcome of the coin toss (heads or tails).
# Step 6: Generate a random number (0 or 1) to represent the outcome of the coin toss. (If the number is 0, the outcome is heads. If it's 1, the outcome is tails.)
# Step 7: Compare the player's guess with the generated outcome.
# Step 8: Increment the correct and total number of guesses


import random

total_guesses = 0
correct_guesses = 0

while True:
    guess = input("Welcome to coin toss game. Please write your guess - head or tail? If you want to stop the game, write 'quit': ")

    if guess == 'quit':
        print('The game has been stopped.')
        break
    else:
        random_number = random.randint(0, 1)
        if random_number == 0 and guess == 'head':
          correct_guesses += 1
          total_guesses += 1
          print(f'Congratulations! You have guessed correctly: {guess}. Attempts tryed: {total_guesses}, correct guesses: {correct_guesses}')
            
        elif random_number == 1 and guess == 'tail':
          correct_guesses += 1
          total_guesses += 1
          print(f'Congratulations! You have guessed correctly: {guess}. Attempts tryed: {total_guesses}, correct guesses: {correct_guesses}')
        
        else:
          total_guesses += 1
          print(f'Try again. Your guess was incorrect. Attempts tryed: {total_guesses}, correct guesses: {correct_guesses}')

print(f'You made a total of {total_guesses} guesses, and {correct_guesses} of them were correct.')
