#John Gouwar, Aryman Babber, Ian Garinger 
#Deck.py
#May 14 2016
#An implementation of the Deck class 
import random

class Card:
    def __init__(self, suit, number):
        self._suit   = suit
        self._number = number
        self._card = []
        
        #set arrays to avoid using too much flow control
        self._suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self._cardList = ["Ace", "2", "3","4","5","6","7","8","9","10","Jack","Queen","King"]

    def getCard(self):
        #each card will be an array with three values
        self._card = []
        #the first will be a string that is outputted to the user when referring to the cards
        self._card.append(self._cardList[self._number] + " of " + self._suits[self._suit])
        
        #the other two will be integers associated with which number and suit the card is for reference
        self._card.append(self._number)
        self._card.append(self._suit)
        return self._card

class Deck:
    def __init__(self):
        
        #the deck is an array of cards
        self._deck = []
        #two  for loops for suit and number
        for i in range(4):
            for j in range(13):
                card = Card(i, j)
                #uses the card class using the ideces of the loops
                self._deck.append(card.getCard())
    #returns the deck            
    def getDeck(self):
        return self._deck

    #shuffles the deck
    def deckShuffle(self):
        random.shuffle(self._deck)
