from deck import Deck
from player import Player

class Game:

    def __init__(self, numOfPlayers, initalChipCount):
        self.deck = Deck()
        self.numOfPlayers = numOfPlayers
        self.prizePool = numOfPlayers * initialChipCount
        self.currentPot = 0
        self.currentCallAmount = 0
        self.players = []
        self.activePlayers = []
        for i in range(numOfPlayers):
            self.players.append(Player(i, initalChipCount))

    def begin(self):
        while self.determineWinner() < 1:
            self.playHand()
        print('Player {} wins!'.format(self.determineWinner()))

    def playHand(self):
        self.deck.resetDeck()
        self.resetActivePlayers()
        self.dealHand()
        self.takeBets()
    
    def dealHand(self):
        for i in range(5):
            for player in self.activePlayers:
                player.receiveCard(self.deck.drawCard())
        for player in self.players:
            print('Player {} hand is: {}\n'.format(player.number, player.hand))

    def takeBets(self):
        for player in self.activePlayers:
            play = self.queryPlay(currentCallAmount)
            if play == 'C':
                player.bet(currentCallAmount)
                self.currentPot += currentCallAmount
            elif play == 'R':
                raiseAmount = self.queryRaise()
                currentCallAmount += raiseAmount
                player.bet(
           else:
                self.activePlayers.remove(player) 
            currentot += player.bet

    def queryPlay(self):
        play = input('Enter F to fold, C to call, or R to raise: ')
        while(play != 'F' && play != 'C' && play != 'R'):
            play = input('Enter F to fold, C to call, or R to raise: ')
        return play

    def queryRaise(self);
        amount = input('Enter raise amount: ')
        return amount

    def determineWinner(self):
        for player in self.players:
            if player.chipCount == self.prizePool:
                return player.number
        return 0

    def resetActivePlayers(self):
        for player in self.players:
            if player.chipCount > 0:
                self.activePlayers.append(player)


numOfPlayers = input('Enter number of players: ')
initialChipCount = input('Enter player initial chip count: ')
instance = Game(int(numOfPlayers), int(initialChipCount))
instance.begin()
