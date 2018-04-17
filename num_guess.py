import random

list_of_guesses = []

rand_num = random.randint(1,70)

guess = int(input('Enter a # between 1-70: '))
list_of_guesses.append(guess)

while guess != rand_num:
    if guess > rand_num:
        print('Your guess is too high!')

    else:
        print('Your guess is too low!')
    guess = int(input('Enter a # between 1-70: '))
    list_of_guesses.append(guess)

else:
    print('You have guessed right! Good job!')
    print('It took you %i guesses' %len(list_of_guesses))
    print('These were your guesses: ')
    print(list_of_guesses)
   