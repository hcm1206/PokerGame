import random

# 카드 덱 리스트의 숫자를 처리하는 클래스
class Cards():
    # 52개의 카드 숫자 덱 리스트 생성
    def __init__(self):
        self.deck = [x for x in range(52)]
        self.index = 0

    # 카드 덱의 숫자 섞기
    def shuffleDeck(self):
        random.shuffle(self.deck)

    # 유저의 최초 카드 2장의 숫자를 덱에서 뽑아서 결정
    def drawMyCard(self):
        myCard = []
        for i in range(2):
            myCard.append(self.drawOneCard())
        return myCard

    # 상대방의 최초 카드 2장의 숫자를 덱에서 뽑아서 결정
    def drawCpuCard(self):
        cpuCard = []
        for i in range(2):
            cpuCard.append(self.drawOneCard())
        return cpuCard
    
    # 최초 공용카드 5장의 숫자를 덱에서 뽑아서 결정
    def drawInitCommonCard(self):
        commonCard = []
        for i in range(5):
            commonCard.append(self.drawOneCard())
        return commonCard

    def drawOneCard(self):
        card = self.deck[self.index]
        self.index += 1
        return card
        










