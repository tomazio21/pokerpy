import random

class Deck:

    def __init__(self):
        self.cards = []

    def generateCards(self):
        suits = ['H', 'D', 'C', 'S']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [value+suit for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)
    
    def resetDeck(self):
        self.generateCards()
        self.shuffle()

    def drawCard(self):
        return self.cards.pop()
