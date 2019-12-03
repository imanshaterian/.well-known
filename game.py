import random
# get a name for game
playerName = input('please enter your name:\n')
# saying hi to player
print('hi {} you have 100 chance to guess the number i choose between 1 and 100 :)\n'.format(playerName))
# the program chooses a number between 1 and 100
finalNumber = random.randrange(1, 101)
# get a number from player
guessedNumber = int(input('please enter your guess:\n'))
# a for loop to analyze the entered number
# with four steps
for i in range(0, 100):
    # step one : if player guess the right number
    if guessedNumber == finalNumber:
        print('nice you guessed it . well played;)\n')
        break
    # step two : if the player guess a larger number than the answer
    elif guessedNumber > finalNumber:
        guessedNumber = int(input('please guess lower:\n'))
        continue
    # step three : if the player guess the smaller number than the answer
    elif guessedNumber < finalNumber:
        guessedNumber = int(input('please guess higher:\n'))
        continue
    # step four : if the player type a incorrect character
    else:
        guessedNumber = int(input('unknown character please type only integer numbers:\n'))
        continue
