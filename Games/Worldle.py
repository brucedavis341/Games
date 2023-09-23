import random
list_of_words = ['money','carry','parry','paris']
random = random.randint(0,len(list_of_words)-1)
hidden_word = '_____'
actual_word = list_of_words[random]
tries = 0
#removes letter, well just move them down with the guess of the letter
def addLetter(hidden_word, guess, n):
    return hidden_word[:n] + guess[n] + hidden_word[n:len(hidden_word)-1]
#if the guess doesnt match the index, it get replaced with '_'
def sameLetter(hidden_word, n):
    return hidden_word[:n] + '_' + hidden_word[n:len(hidden_word)-1]
#determines the amount of guesses and as well as if the guess matches or if its the same as the letter already chosen
def manyGuesses():#
    global tries 
    global hidden_word 
    global actual_word
    while tries < 5:
        if tries == 0:
            print('Okay here\'s your first guess.')
            guess = input('What do you think the word is? ')
            if len(guess) > 5:
                print('Less than five letter, and do number if you want.\n Not my fault if you lose.')
                manyGuesses()
        else:
            print('Let\'s try another guess.')
            guess = input('What do you think the word is? ')
        for index in range(0,len(hidden_word)):
            if guess[index] == actual_word[index] and guess[index] != hidden_word[index]:
                hidden_word = addLetter(hidden_word, guess, index)
            elif hidden_word[index] == actual_word[index] and guess[index] == hidden_word[index]:
                pass
            elif hidden_word[index] == actual_word[index] and guess[index] != hidden_word[index]:
                pass
            else:
                hidden_word = sameLetter(hidden_word, index)
        tries += 1
        print('Let\'s see if any letters got revealed\n','\t', '[' + hidden_word + ']')
        if hidden_word == actual_word and tries < 5:
            print(' You guessed the word, you must be real good!')
            break
        tries += 1
    if hidden_word == actual_word and tries == 5:
        print('You guessed the word!')
    elif hidden_word != actual_word and tries == 5:
        print('Dang, you didn\'t guessed the word')

def Game():
    print('\t\t\tWelcome to my Wordle Game')
    print('Rules')
    print('Guess the word with only in five letter intervals\n')
    print('Here is your word that you have to guess\n', '[' + hidden_word + ']')
    manyGuesses()

Game()
