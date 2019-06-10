import random

class Card:
    'represents a playing card'
    def __init__(self, rank, suit):
        'initialize rank and suit of playing card'
        self.rank = rank
        self.suit = suit
    def getRank(self):
        'return rank'
        return self.rank
    def getSuit(self):
        'return suit'
        return self.suit

class Deck:
    'represents a deck of 52 cards'
    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    # suits is a set of 4 Unicode symbols representing the 4 suits
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = [] # deck is initially empty
        for suit in Deck.suits: # suits and ranks are Deck 
            for rank in Deck.ranks: # class variables
        # add Card with given rank and suit to deck
                self.deck.append(Card(rank, suit))
    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        if len(self.deck)== 0:
            raise OutOfCards()
        else:
            return self.deck.pop()
    def shuffle(self):
        'shuffle the deck'
        shuffle(self.deck)

class Hand:
    def __init__(self):
        'represents the player hand'
        house = []  # house hand
        player = [] # player hand
    def initialHand(house,player):
        for i in range(2):        # dealing initial hands in 2 rounds
            Deck.dealCard(deck, player)    # deal to player first
            Deck.dealCard(deck, house)     # deal to house second
    def printHands(house, player):
          # print hands
        print('House:{:>7}{:>7}'.format(house[0], house[1]))
        print(' You:{:>7}{:>7}'.format(player[0], player[1]))
        
    def total(hand):
      'returns the value of the blackjack hand'
      values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
      '9':9, '1':10, 'J':10, 'Q':10, 'K':10, 'A':11}
      result = 0
      numAces = 0

      # add up the values of the cards in the hand
      # also add the number of aces
      for card in hand:
            result += values[card[0]]
            if card[0] == 'A':
                  numAces += 1
      # while value of hand is > 21 and there is an ace
      # in the hand with value 11, convert its value to 1
      while result > 21 and numAces > 0:
            result -= 10
            numAces -= 1

      return result

    def compareHands(house, player, score):
        'compares house and player hands and prints outcome'
        # compute house and player hand total
        houseTotal, playerTotal = total(house), total(player)
        if houseTotal > playerTotal:
                print('You lose.')
                score[0]+=1
        elif houseTotal < playerTotal:
                print('You win.')
                score[1]+=1
        elif houseTotal == 21 and 2 == len(house) < len(player):
                print('You lose.') # house wins with a blackjack
                score[0]+=1
        elif playerTotal == 21 and 2 == len(player) < len(house):
                print('You win.') # players wins with a blackjack
                score[1]+=1
        else:
                print('A tie.')
class Record:
    'represents the win/loss record'
    def __init__(self, housewins=0, playerwins=0):
        'initialize win/loss record'
        self.housewins = housewins
        self.playerwins = playerwins
    def getHouseWins(self):
        'return housewins'
        return self.housewins
    def increaseHouseScore(self):
        'change house wins'
        self.housewins = housewins +1
        return housewins
    def increasePlayerScore(self):
        'return playerwins'
        self.playerwins = playerwins +1
        return playerwins
    def getRecord(self):
        return [housewins,playerwins]
    def printRecord(self):
    	print('The Game is over! You have won', self.playerwins, ' games and the\
        dealer has won ',self.housewins,' games')
    	if self.housewins>self.playerwins:
    		print('You lost overall')
    	elif self.housewins<self.playerwins:
    		print('You won overall')
    	elif self.housewins==self.playerwins:
    		print('You tied overall')

    #compare hands here?

class OutOfCards(Exception):
    'Out of cards'
    pass

class Blackjack:
    'mechanics of actual game'
    def __init__(self):
        
        deck = Deck()
##        self.player = player
##        self.house = house
        player = Hand()
        house = Hand()
    #def play():
    while(True):
            house = []  # house hand
            player = [] # player hand
            deck = Deck()
            deck=deck.shuffle()
            for i in range(2):        # dealing initial hands in 2 rounds
                    try:
                        dealCard(deck, player)    # deal to player first
                    except OutOfCards:
                        winRecord = Record()
                        winRecord.printRecord()  
                    except:
                        print('something else is wrong')
                    try:
                        dealCard(deck, house)    
                    except OutOfCards:
                        winRecord = Record()
                        winRecord.printRecord()    # deal to house second
                    except:
                        print('something else is wrong')
                
            # print hands
            print('House:{:>7}{:>7}'.format(house[0], house[1]))
            print(' You:{:>7}{:>7}'.format(player[0], player[1]))

            # while user requests an additional card, house deals it
            answer = input('Hit or stand? (default: hit): ')
            #answer = getinput(total(house), total(player))
            while answer in {'', 'h', 'hit'}:
                    try:
                        card = dealCard(deck, player)
                    except OutOfCards:
                        winRecord = Record()
                        winRecord.printRecord()    # deal to player
                    print('You got{:>7}'.format(card))

                    if total(player) > 21:         # player total is > 21
                          print('You went over… You lose.')
                          break
                    else:
                          answer = input('Hit or stand? (default: hit): ')
                    #answer = getinput(total(house), total(player))

            # house must play the “house rules”
            if(total(player))<21:
                    while total(house) < 17:
                            try:
                                card = dealCard(deck, house)
                            except OutOfCards:
                                winRecord = Record()
                                winRecord.printRecord()

                            print('House got{:>7}'.format(card))

                            if total(house) > 21: # house total is > 21
                                    print('House went over… You win.')
                                    break
                    compareHands(house, player)

                    # compare house and player hands and print result




