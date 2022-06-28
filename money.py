class MoneyInfo:
    def __init__(self):
        self.money = 10000
        self.blindamount = 100
        self.minimumBatting = self.blindamount
        self.totalBatting = 0
    
    def newGame(self):
        self.minimumBatting = self.blindamount
        self.totalBatting = 0
    
    def blind(self):
        self.money -= self.blindamount
        self.totalBatting += self.blindamount

    def addBatting(self, amount):
        self.money -= amount
        self.totalBatting += amount
        self.minimumBatting = amount
    
    def allIn(self):
        self.totalBatting += self.money
        self.money = 0

    def addMoney(self, acount):
        self.money += acount


    def getTotalBatting(self):
        return self.totalBatting
    
    def getMinimumBatting(self):
        return self.minimumBatting

    def getMoney(self):
        return self.money


    