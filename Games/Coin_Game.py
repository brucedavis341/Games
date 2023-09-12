def Game(coins): 
    if coins == 21:
        print('Welcome to the Coin Game\n', 'Rules: Try to be the last one to take the coins.\n', 'Only take the coins in 1s 2s or 3s\n', 'Lastly have some fun!!!')
        coins = oneRound(coins)
        return Game(coins)
    elif coins > 0:
        coins = oneRound(coins)
        return Game(coins)
    else:
        return 0
      
        
    
    
def oneRound(n):
    n = userMove(n)
    if n == 0:
        return 'You have a won'
    n = botMove(n)
    if n == 0:
        return 'You have won!'
    print('There are ' + str(n) +' coins on the table.\n')
    return n
      
    
    
    
def userMove(n):
    user = int(input('How many coins do you want to take? '))
    if user == 1:
      n -=1
      print('You have taken 1 coin.')
      print('There are ' + str(n) +' coins on the table.')
      return n
    elif user == 2:
      n -= 2
      print('You have taken 2 coins.')
      print('There are ' + str(n) +' coins on the table.')
      return n
    else:
      n -= 3
      print('You have taken 3 coins.')
      print('There are ' + str(n) +' coins on the table.')
      return n
      
        
def botMove(n):
    if n % 4 == 0 or n % 2 == 0:
      n -= 2
      print('I have taken 2 coins.')
      print('There are ' + str(n) +' coins on the table.')
      return n
    elif n % 4 == 1:
      n -= 1
      print('I have taken 1 coins.')
      print('There are ' + str(n) +' coins on the table.')
      return n
    else:
      n -= 3
      print('I have taken 3 coins.')
      print('There are ' + str(n) +' coins on the table.')
      return n
        

Game(21)
