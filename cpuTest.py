from CheckJokbo import checkJokbo
import random

class PrototypeAI:
    def __init__(self, game):
        self.nowDeck = []
        self.game = game
        
    def initCard(self):
        self.nowDeck = []

    def addCard(self, newCard):
        self.nowDeck.append(newCard)
    
    def bettingReply(self, playerBetting):
        if self.game.AIBetting == True:
            return True
        comDeck = self.nowDeck[2:]
        jokbo, score = checkJokbo(self.nowDeck)
        if comDeck:
            comJokbo, comScore = checkJokbo(comDeck)
            if self.game.turn == 4 and playerBetting >= 1000:
                if (score >= 300 and comScore < 300) or score >= 500:
                    return True
                else:
                    return False
            else:
                if score >= 200:
                    return True
                else:
                    return False
        if sum(self.nowDeck) >= 30 or score >= 200:
            return True
        else:
            return False

    def allInReply(self):
        if self.game.AIBetting == True:
            return True
        jokbo, score = checkJokbo(self.nowDeck)
        if self.game.turn == 1:
            if score >= 200:
                return True
            else:
                return False
        else:
            if score >= 500:
                return True
            else:
                return False

    def whetherBetting(self):
        comDeck = self.nowDeck[2:]
        jokbo, score = checkJokbo(self.nowDeck)
        if comDeck:
            comJokbo, comScore = checkJokbo(comDeck)
        if self.chance(score/10):
            if self.chance(((score/100)**2)/2):
                self.game.AIBetting = True
                return self.game.cpuMoneyInfo.getMoney()
            if comDeck:
                if score > 300 and comScore < 300:
                    self.game.AIBetting = True
                    return max([100, int(score/100)*500 + self.randomMoneyAdd()])
                elif self.chance(score/5):
                    self.game.AIBetting = True
                    return max([100, int(score/100)*500 + self.randomMoneyAdd()])
        return 0


    def chance(self, percentage):
        if random.randrange(0,100) < percentage:
            return True
        else:
            return False

    def randomMoneyAdd(self):
        return int(random.random() * 10) * 200 - 1000