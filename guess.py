import random

# Create the random number
secret_number = random.randint(1,100)

count = 0
while True:
    # Ask for a guess
    guess = int(input('Guess a number between 1 and 100: '))
    count += 1

    # Check if the guess is correct or need adjustments
    if guess < secret_number:
        print('Higher..')
    elif guess > secret_number:
        print('Lower..')
    else:
        print(f'Correct! Guessed in {count} times')
        break