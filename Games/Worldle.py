import random
from termcolor import colored
guessed_words = ['_|_|_|_|_','_|_|_|_|_','_|_|_|_|_','_|_|_|_|_','_|_|_|_|_',]
guess = ''
tries = 0

def getRandomWord():
    with open("Games/words.txt", "r") as file: 
        data = file.read() 
        words = data.split() 
    pick = random.randint(0,len(words)-1)
    return words[pick]


def gameScreen():
    global guessed_words
    print('Let\'s see if any letters got revealed')
    for i in range(0,len(guessed_words)):
        print('\t', '[' + guessed_words[i] + ']')

def checkGuess(guess,answer):
    new_word = ''
    for i in range(len(answer)):
        if i != len(answer)-1:
            if guess[i] != answer[i] and guess[i] not in answer or guess[i] in new_word:
                new_word += colored(guess[i].upper(), 'red', attrs=["bold"]) + '|'
            elif guess[i] != answer[i] and guess[i] in answer:
                new_word += colored(guess[i].upper(), 'yellow', attrs=["bold"]) + '|'
            else:
                new_word += colored(guess[i].upper(), 'green', attrs=["bold"]) + '|'
        else:
            if guess[i] != answer[i] and guess[i] not in answer or guess[i] in new_word:
                new_word += colored(guess[i].upper(), 'red', attrs=["bold"])
            elif guess[i] != answer[i] and guess[i] in answer:
                new_word += colored(guess[i].upper(), 'yellow', attrs=["bold"])
            else:
                new_word += colored(guess[i].upper(), 'green', attrs=["bold"])
    return new_word
    


def manyGuesses(tries):
    while tries != 5:
        guess = input('What do you think the word is? ')
        if len(guess) > 5:
            print('Too many letters; only five!')
            manyGuesses(tries)
        elif len(guess) < 5:
            print('Too little letters; only five!')
            manyGuesses(tries)
        else:
            guessed_words[tries] = checkGuess(guess,answer)
            gameScreen()
        if guess == answer:
            print('You win, great job!!!')
            break
        tries += 1
    if tries == 5:
        print('You lose, good try I guess. The word was', answer + '.') 


def Game():
    global answer
    print('\t\t\tWelcome to my Wordle Game')
    print('Rules')
    print('Guess the word with only in five letter intervals')
    print('Here is the word; sorry its hidden!!!\n','\t', '[_____]')
    answer = getRandomWord()
    manyGuesses(tries)
    replay = input('Do you want to play again?(Y/N) ')
    if replay.upper() == 'Y':
        Game()
    else:
        print('Thanks for playing!!!')

Game()
