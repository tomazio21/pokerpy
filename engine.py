from collections import defaultdict

class BettingEngine:

    def __init__(self, prizePool, smallBlind):
        self.prizePool = 0
        self.smallBlindAmount = smallBlind
        self.pot = 0
        self.callAmount = 0
        self.activePlayerBets = defaultdict(lambda: -1)

    def bet(self, player, amount):
        player.bet(amount)
        self.pot += amount
        self.activePlayerBets[player] = amount

    def resetPot(self):
        self.pot = 0
        self.callAmount = 0
        self.activePlayerBets = defaultdict(lambda: -1)

    def resetActivePlayerBets(self):
        self.activePlayerBets = defaultdict(lambda: -1)

    def resetCallAmount(self):
        self.callAmount = 0

    def getActivePlayers(self):
        return list(self.activePlayerBets.keys())

    def collectBlinds(self, smallBlindBettor, bigBlindBettor):
        smallBlindAmount = self.smallBlindAmount
        self.bet(smallBlindBettor, smallBlindAmount)

        bigBlindAmount = self.smallBlindAmount * 2
        self.bet(bigBlindBettor, bigBlindAmount)

    def check(self, player):
        self.bet(player, 0)

    def call(self, player):
        self.bet(player, self.callAmount)

    def raise_(self, player, raiseAmount):
        self.bet(player, self.callAmount + raiseAmount)
        self.callAmount += raiseAmount

    def fold(self, player):
        if self.activePlayerBets[player] > -1:
            player.resetHand()
            del self.activePlayerBets[player]

    def allBetsNotEqual(self):
        if len(self.activePlayerBets) == 1:
            return false
        bets = list(self.activePlayerBets.values())
        result = bets[0]
        for bet in bets[1:]:
            result = result ^ bet
        return result != 0
