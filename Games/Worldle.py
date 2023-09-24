import random
list_of_words = ['money','carry','parry','paris']
random = random.randint(0,len(list_of_words)-1)
hidden_word = '_____'
actual_word = list_of_words[random]
tries = 0

def addLetter(hidden_word, guess, n):
    return hidden_word[:n] + guess[n] + hidden_word[n:len(hidden_word)-1]

def sameLetter(hidden_word, n):
    return hidden_word[:n] + '_' + hidden_word[n:len(hidden_word)-1]

def checkGuess(guess,hidden_word):
    for index in range(0,len(hidden_word)):
        if guess[index] == actual_word[index] and guess[index] != hidden_word[index]:
            hidden_word = addLetter(hidden_word, guess, index)
        elif hidden_word[index] == actual_word[index] and guess[index] == hidden_word[index]:
            pass
        elif hidden_word[index] == actual_word[index] and guess[index] != hidden_word[index]:
            pass
        else:
            hidden_word = sameLetter(hidden_word, index)
    return hidden_word

def manyGuesses():
    global tries 
    global hidden_word 
    global actual_word
    global guess
    global early_game
    while tries < 5:
        if tries == 0:
            print('Okay here\'s your first guess.')
            guess = input('What do you think the word is? ')
            if len(guess) > 5:
                print('Less than five letter, and guess a number if you want.\nNot my fault if you lose.')
                guess = ''
                manyGuesses()
            else:
                hidden_word = checkGuess(guess,hidden_word)
                print('Let\'s see if any letters got revealed\n','\t', '[' + hidden_word + ']')
                if hidden_word == actual_word:
                    print(' You guessed the word, you must be real good!')
                    tries = 5
                    early_game = 5
                    break
                else:
                    tries += 1
                    manyGuesses()
        elif tries >= 1:
            print('Let\'s try another guess.')
            guess = input('What do you think the word is? ')
            if len(guess) > 5:
                print('Less than five letter, and guess a number if you want.\nNot my fault if you lose.')
                guess = ''
                manyGuesses()
            else:
                hidden_word = checkGuess(guess,hidden_word)
                print('Let\'s see if any letters got revealed\n','\t', '[' + hidden_word + ']')
                if hidden_word == actual_word:
                    print(' You guessed the word, you must be real good!')
                    tries = 5
                    early_game = 5
                    break
                else:
                    tries += 1
                    manyGuesses()
    if hidden_word == actual_word and tries == 5 and early_game == 0:
        print('You guessed the word!')
    elif hidden_word != actual_word and tries == 5 and early_game == 0:
        print('Dang, you didnt guessed the word')
    else:
        pass

def Game():
    print('\t\t\tWelcome to my Wordle Game')
    print('Rules')
    print('Guess the word with only in five letter intervals')
    print('Here is your word that you have to guess\n', '[' + hidden_word + ']')
    manyGuesses()

Game()
