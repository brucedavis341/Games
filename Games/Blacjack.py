import random

cardsVal = {'1D': 1, '2D': 2, '3D': 3, '4D': 4, '5D': 5, '6D': 6, '7D': 7, '8D': 8, '9D': 9, '10D': 10,
            '1S': 1, '2S': 2, '3S': 3, '4S': 4, '5S': 5, '6S': 6, '7S': 7, '8S': 8, '9S': 9, '10S': 10,
            '1C': 1, '2C': 2, '3C': 3, '4C': 4, '5C': 5, '6C': 6, '7C': 7, '8C': 8, '9C': 9, '10C': 10,
            '1H': 1, '2H': 2, '3H': 3, '4H': 4, '5D': 5, '6D': 6, '7D': 7, '8D': 8, '9D': 9, '10D': 10,
            'AS': 11, 'AD': 11, 'AH': 11, 'AC': 11, 'KS': 10, 'KH': 10, 'KC': 10, 'KD': 10, 'QS': 10,
            'QH': 10, 'QD': 10, 'QC': 10, 'JS': 10, 'JD': 10, 'JC': 10, 'JH': 10}

def dealer(cards, handvalues):
    random_card = random.randint(0,len(cards)-2)#Allows the number to be update after card has been took
    random_card2 = random.randint(0,len(cards)-2)
    if len(dealerhand) < 1:
        dealerhand.append(cards[random_card])#Takes the cards from the deck
        cards.remove(cards[random_card])#removes the card that was picked
        dealerhand.append(cards[random_card2])
        cards.remove(cards[random_card2])
        print('The dealer has his deck.')
        return handvalues[dealerhand[0]] + handvalues[dealerhand[1]]
    elif dealerScore >= 10 and dealerScore <= 17:
        dealerhand.append(cards[random_card])
        cards.remove(cards[random_card])
        print('The dealer has recieved one card.')
        return dealerScore + handvalues[dealerhand[len(dealerhand)-1]]    
    else:
        print('The dealer didnt want anymore cards.')
        return dealerScore

def player(cards, handvalues):
    random_card = random.randint(0,len(cards)-2)
    random_card2 = random.randint(0,len(cards)-2)
    if len(playerhand) < 1:
        playerhand.append(cards[random_card])
        cards.remove(cards[random_card])
        playerhand.append(cards[random_card2])
        cards.remove(cards[random_card2])
        print('Here is your Deck: ', playerhand)
        return handvalues[playerhand[0]] + handvalues[playerhand[1]]
    elif len(playerhand) >= 2:
        playerhand.append(cards[random_card])
        cards.remove(cards[random_card])
        print(playerhand)
        return userScore + handvalues[playerhand[len(playerhand)-1]]
        
    

            
                

def oneRound():
    global userScore
    global dealerScore
    dealerScore = dealer(cards, cardsVal)
    if dealerScore > 21:# if the dealer bust, the player wins
        print('The dealer bust, so you win!')
    userScore = player(cards, cardsVal)
    for card in playerhand:
        if card == 'AS' or card == 'AC' or card == 'AH' or card == 'AD':#Sees what value the user wants the Ace to be
            aceValue = input('What is the value of your ace; 11 or 1(1 for 11, 2 for 1): ')
            if aceValue == '1':
                continue
            elif aceValue == '2':
                cardsVal[card] = 1
                userScore = userScore - 1
                continue
            else:
                print('You didn\'t follow directions, you keep the value of 11!')
                continue
    if userScore > 21:# if the user bust, the dealer wins; hopefully he it checks it
        print('You bust, the dealer wins!')
    else:
        decision(userScore, dealerScore)

def decision(a, b):
    decision = input('Make your decision. Keep your cards or get one more! (1 for card, 2 for no card) ')
    if decision == '1':
        oneRound()
    elif decision == '2':
        if a > b:
            print('You were the closest to 21. You win!') 
        elif b > a:
            print('The dealer was closest to 21. You lose!')
        else:
            print('It was a tie, ya\'ll both win!')
    else:
        print('Thought you found a bug; let\'s see if you won.')
        if a > b:
            print('You were the closest to 21. You win!') 
        elif b > a:
            print('The dealer was closest to 21. You lose!')
        else:
            print('It was a tie, ya\'ll both win!')

def play_again():
    answer = input('Do you want to play again?(Y/N) ')
    if answer.upper() == 'Y':
        Game()
    elif answer.upper() == 'N':
        print('Thanks for playing!!!!')
    else:
        print('Well...Thanks for playing!!!')


def Game():
    global dealerhand
    global playerhand
    dealerhand = []
    playerhand = []
    cards = ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S',
    '9S', '10S', '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '1H', '2H', '3H', '4H', '5D', '6D',
    '7D', '8D', '9D', '10D', 'AS', 'AD', 'AH', 'AC', 'KS', 'KH', 'KC', 'KD', 'QS', 'QH', 'QD', 'QC', 'JS', 'JD',
    'JC', 'JH']
    print('Welcome to Blackjack!!!!')
    print('Rule:')
    print('1. You will receive two cards that equal up to the value of 4 to 21')
    print('2. You have three ways to win.')
    print('3. The dealer either busts, you get a greater value than the dealer or you get 21.')
    print('4. Also vice versa, so good luck and have fun!')
    oneRound()
    play_again()
Game()
