import random

print('H A N G M A N')

while True:
    words = ('python', 'java', 'kotlin', 'javascript')
    answer = random.choice(words)
    hidden = ['-'] * len(answer)
    guessed_letters = []

    game_on = False
    start = input('Type "play" to play the game, "exit" to quit: ')
    if start == 'play':
        game_on = True
    elif start == 'exit':
        break
    else:
        continue

    guesses = 8
    while guesses != 0 and game_on:
        hidden_string = ''.join(hidden)

        if hidden_string == answer:
            print('You guessed the word {}!'.format(answer))
            print('You survived!')
            break

        print()
        print(hidden_string)
        guess = input('Input a letter: ')

        if len(guess) != 1:
            print('You should print a single letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('It is not an ASCII lowercase letter')
        elif guess in guessed_letters:
            print('You already typed this letter')
        elif guess in answer:
            occurrences = [pos for pos, letter in enumerate(answer) if letter == guess]
            for i in occurrences:
                hidden[i] = guess
        else:
            print('No such letter in the word')
            guesses -= 1

        if guesses == 0:
            print('You are hanged!')
            break

        guessed_letters.append(guess)

    print()
