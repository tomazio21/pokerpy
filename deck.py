import random

def generateDeck():
    suits = ['H', 'D', 'C', 'S']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = [value+suit for suit in suits for value in values]
    random.shuffle(cards)
    return cards

def drawCard(deck):
    return deck.pop()
