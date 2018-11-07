#GuEsS a NuMbEr
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

#6 gUeSsEs
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is low dude.')
    elif guess > secretNumber:
        print('That one is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job! You guessed it in only ' + str(guessesTaken) + ' guesses!')
else:
    print('Totally wrong. It was ' + str(secretNumber))
