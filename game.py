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
        self.currentActivePlayerBets = {}
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
            betAction = self.queryBetAction()
            updateGameState(player, betAction)
        while allBetsNotEqual():
            for player in self.activePlayers:
                betAction = self.queryBetAction()
                updateGameState(player, betAction)
        
    def updateGameState(self, player, betAction):
        if play == 'C':
            player.bet(self.currentCallAmount)
            self.currentPot += currentCallAmount
            self.currentActivePlayerBets[player.number] = self.currentCallAmount 
        elif play == 'R':
            raiseAmount = self.queryRaise()
            currentCallAmount += raiseAmount
            player.bet(currentCallAmount)
            self.currentActivePlayerBets[player.number] = self.currentCallAmount
        elif: play == 'CH':
            self.currentActivePlayerBets[player.number] = 0
        else:
            self.activePlayers.remove(player)
            del self.currentActivePlayerBets[player.number]

    def allBetsNotEqual():
        if len(self.currentActivePlayerBets) == 1:
            return false
        bets = list(self.currentActivePlayerBets.values())
        result = bets[0]
        for bet in bets[1:]:
            result = result ^ bet
        return result != 0

    def queryBetAction(self):
        play = input('Enter F to fold, CH to check, C to call, or R to raise: ')
        while(play != 'F' && play != 'C' && play != 'R' && play != 'CH'):
            play = input('Enter F to fold, CH to check, C to call, or R to raise: ')
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
        self.currentActivePlayerBets = {}

numOfPlayers = input('Enter number of players: ')
initialChipCount = input('Enter player initial chip count: ')
instance = Game(int(numOfPlayers), int(initialChipCount))
instance.begin()
