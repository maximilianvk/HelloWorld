secret_num = 4
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_num:
        print('You did it! You guessed correctly!')
        break
    elif guess > guess_limit:
        print('')
    elif guess != secret_num:
        print('Try Again!')
else:
    print('Better Luck Next time!')
