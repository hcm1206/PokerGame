class MoneyInfo:
    def __init__(self):
        self.money = 10000
        self.blindamount = 100
        self.minimumBetting = self.blindamount
        self.totalBetting = 0
    
    def newGame(self):
        self.minimumBetting = self.blindamount
        self.totalBetting = 0
    
    def blind(self):
        self.money -= self.blindamount
        self.totalBetting += self.blindamount

    def addBetting(self, amount):
        self.money -= amount
        self.totalBetting += amount
        self.minimumBetting = amount
    
    def allIn(self):
        self.totalBetting += self.money
        self.money = 0

    def addMoney(self, acount):
        self.money += acount


    def getTotalBetting(self):
        return self.totalBetting
    
    def getMinimumBetting(self):
        return self.minimumBetting

    def getMoney(self):
        return self.money


    