class MoneyInfo:
    def __init__(self):
        self.originMoney = 10000
        self.money = self.originMoney
        self.blindamount = 100
        self.minimumBetting = 0
        self.totalBetting = 0
    
    def newGame(self):
        self.totalBetting = 0
    
    # 만약 블라인드보다 소지금이 적다면 모든 소지금을 블라인드로 제출하게 됨(음수가 나오지 않게 조정)
    def blind(self):
        if self.money >= self.blindamount:
            self.money -= self.blindamount
            self.totalBetting += self.blindamount
        else:
            self.totalBetting += self.money
            self.money = 0

    def addBetting(self, amount):
        self.money -= amount
        self.totalBetting += amount
    
    def allIn(self, oppositeMoneyInfo):
        oppositeMoney = oppositeMoneyInfo.getMoney()
        myMoney = self.money
        if self.money > oppositeMoney:
            self.addBetting(self.money)
            oppositeMoneyInfo.addBetting(oppositeMoney)
        else:
            self.addBetting(self.money)
            oppositeMoneyInfo.addBetting(myMoney)

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

    def setBlind(self, blind):
        self.blindamount = blind

    def getTotalBetting(self):
        return self.totalBetting
    
    def getMinimumBetting(self):
        return self.minimumBetting

    def getMoney(self):
        return self.money




    


    