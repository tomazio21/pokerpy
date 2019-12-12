class Player:

    def __init__(self, number, chipCount):
        self.hand = []
        self.number = number
        self.chipCount = chipCount 

    def setChipCount(self, amount):
        self.chipCount = amount

    def receiveCard(self, card):
        self.hand.append(card)

    def resetHand(self):
        self.hand = []

    def bet(self, amount):
        self.chipCount -= amount

    def receiveWinnings(self, amount):
        self.chipCount += amount
