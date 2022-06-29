class MoneyInfo:
    def __init__(self):
        self.originMoney = 10000
        self.money = self.originMoney
        self.blindamount = 100
        self.minimumBetting = 0
        self.totalBetting = 0
    
    def newGame(self):
        self.totalBetting = 0
    
    def blind(self):
        self.money -= self.blindamount
        self.totalBetting += self.blindamount

    def addBetting(self, amount):
        self.money -= amount
        self.totalBetting += amount
    
    def allIn(self):
        self.totalBetting += self.money
        self.money = 0

    def addMoney(self, acount):
        self.money += acount

    def setMinimumBetting(self, amount):
        self.minimumBetting = amount

    def initMinimumBetting(self):
        self.minimumBetting = 0
    
    def initMoney(self):
        self.money = self.originMoney

    def getBlindAmount(self):
        return self.blindamount

    def getTotalBetting(self):
        return self.totalBetting
    
    def getMinimumBetting(self):
        return self.minimumBetting

    def getMoney(self):
        return self.money

    


    