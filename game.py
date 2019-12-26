from deck import generateDeck, drawCard
from player import Player
from engine import BettingEngine

class Game:

    def __init__(self, numOfPlayers, initalChipCount, smallBlind):
        self.bettingEngine = BettingEngine(numOfPlayers * initialChipCount, smallBlind)
        self.smallBlindBettor = 0
        self.players = []
        for i in range(1, numOfPlayers + 1):
            self.players.append(Player(i, initalChipCount))

    def begin(self):
        while not self.winnerDetermined(self.bettingEngine.prizePool):
            self.playHand(self.players, self.bettingEngine)
        print('Player {} wins!'.format(self.determineWinner()))

    def playHand(self, players, bettingEngine):
        field = []
        deck = generateDeck()

        smallBlindBettor = self.getSmallBlindBettor(players)
        bigBlindBettor = self.getBigBlindBettor(players)
        bettingEngine.collectBlinds(smallBlindBettor, bigBlindBettor)

        self.dealHand(deck, players)
        self.takeBets(self.getActivePlayers(players), bettingEngine)

        #burn card
        drawCard(deck)
        for i in range(3):
            field.append(drawCard(deck))
        print('the field is: ')
        print(field)

        bettingEngine.resetActivePlayerBets()
        bettingEngine.resetCallAmount()
        self.takeBets(self.getActivePlayers(players), bettingEngine)

        #burn card
        drawCard(deck)
        turnCard = drawCard(deck)
        field.append(turnCard)
        print('the field is: ')
        print(field)

        bettingEngine.resetActivePlayerBets()
        bettingEngine.resetCallAmount()
        self.takeBets(self.getActivePlayers(players), bettingEngine)

        #burn card
        drawCard(deck)
        riverCard = drawCard(deck)
        field.append(riverCard)
        print('the field is: ')
        print(field)

        bettingEngine.resetActivePlayerBets()
        bettingEngine.resetCallAmount()
        self.takeBets(self.getActivePlayers(players), bettingEngine)

        #handWinner = determineHandWinner(bettingEngine.getActivePlayers(players), field)
        #handWinner.receiveWinnings(bettingEngine.pot)

        self.incrementSmallBlindBettor(players)
        bettingEngine.resetPot()
        for player in players:
            player.resetHand()
    
    def getSmallBlindBettor(self, players):
        return players[self.smallBlindBettor]

    def getBigBlindBettor(self, players):
        index = self.smallBlindBettor + 1
        if index == len(players):
            index = 0

        while players[index].chipCount == 0:
            index += 1
            if index == len(players):
                index = 0

        return players[index]

    def incrementSmallBlindBettor(self, players):
        index = self.smallBlindBettor + 1
        if index == len(players):
            index = 0

        while players[index].chipCount == 0:
            index += 1
            if index == len(players):
                index = 0

        self.smallBlindBettor = index

    def getActivePlayers(self, players):
        activePlayers = []
        for player in players:
            if len(player.hand):
                activePlayers.append(player)
        return activePlayers
   
    def dealHand(self, deck, players):
        for i in range(2):
            for player in players:
                if player.chipCount > 0:
                    player.receiveCard(drawCard(deck))
        for player in self.players:
            print('Player {} hand is: {}\n'.format(player.identifier, player.hand))

    def takeBets(self, players, bettingEngine):
        for player in players:
            action = self.queryBetAction(player, bettingEngine.pot, bettingEngine.callAmount)
            self.performBetAction(player, action, bettingEngine)

        for player in bettingEngine.activePlayerBets.keys():
            if bettingEngine.allBetsNotEqual():
                action = self.queryBetAction(player, bettingEngine.pot, bettingEngine.callAmount)
                self.performBetAction(player, action, bettingEngine)
            else:
                break

    def performBetAction(self, player, action, bettingEngine):
        if action == 'C':
            bettingEngine.call(player)
        elif action == 'R':
            raiseAmount = self.queryRaise()
            bettingEngine.raise_(player, raiseAmount)
        elif action == 'CH':
            bettingEngine.check(player)
        else:
            bettingEngine.fold(player)

    def queryBetAction(self, player, pot, callAmount):
        message = ''
        print('Current pot: {}    Call Amount: {}    Current chip count: {}'.format(pot, callAmount, player.chipCount))
        if callAmount == 0:
            message = 'Player {}, enter F to fold, CH to check, C to call, or R to raise: '.format(player.identifier)
        else:
            message = 'Player {}, enter F to fold, C to call, or R to raise: '.format(player.identifier)
        play = input(message)
        while(play != 'F' and play != 'C' and play != 'R' and play != 'CH'):
            play = input(message)
        return play

    def queryRaise(self):
        amount = input('Enter raise amount: ')
        return int(amount)

    def winnerDetermined(self, prizePool):
        for player in self.players:
            if player.chipCount == prizePool:
                return player.identifier
        return 0

numOfPlayers = input('Enter number of players: ')
initialChipCount = input('Enter player initial chip count: ')
smallBlindAmount = input('Enter small blind amount: ')
instance = Game(int(numOfPlayers), int(initialChipCount), int(smallBlindAmount))
instance.begin()
