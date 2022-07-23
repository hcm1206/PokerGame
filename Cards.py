# 카드 덱 객체에 관한 클래스와 메소드
# 이 클래스 내에는 카드 정보(리스트의 숫자)만 다룸

import random

# 카드 덱 리스트의 숫자를 처리하는 클래스
class Cards:
    # 52개의 카드 숫자 덱 리스트 생성
    def __init__(self):
        self.deck = [x for x in range(52)] # 0부터 51까지 숫자 리스트 생성
        self.initDeck()

    def initDeck(self):
        self.shuffleDeck()
        self.index = 0 # 현재 뽑아야 할 카드의 인덱스 번호 (처음에는 하나도 안 뽑았으므로 0번째 인덱스의 카드부터 뽑음)
        self.myDeckCards = []
        self.cpuDeckCards = []
        self.commonDeckCards = [] 

    # 카드 덱의 숫자 섞기
    def shuffleDeck(self):
        random.shuffle(self.deck)

    # 유저의 최초 카드 2장의 숫자를 덱에서 뽑아서 결정
    def drawMyCard(self):
        myCard = []
        for i in range(2):
            card = self.drawOneCard()
            myCard.append(card)
            self.myDeckCards.append(card)
        return myCard

    # 상대방의 최초 카드 2장의 숫자를 덱에서 뽑아서 결정
    def drawCpuCard(self):
        cpuCard = []
        for i in range(2):
            card = self.drawOneCard()
            cpuCard.append(card)
            self.cpuDeckCards.append(card)
        return cpuCard
    
    # 최초 공용카드 5장의 숫자를 덱에서 뽑아서 결정
    def drawInitCommonCard(self):
        commonCard = []
        for i in range(5):
            card = self.drawOneCard()
            commonCard.append(card)
            self.commonDeckCards.append(card)
        return commonCard

    # 카드 한 장을 덱에서 뽑아 리턴하는 메소드
    def drawOneCard(self):
        card = self.deck[self.index]
        self.index += 1
        return card


    # 본인 패의 카드 2장 정보 리스트로 출력
    def getMyDeckCards(self):
        return self.myDeckCards

    # 상대방 패의 카드 2장 정보 리스트로 출력
    def getCpuDeckCards(self):
        return self.cpuDeckCards

    # 커뮤니티 카드 2장 정보 리스트로 출력
    def getCommonDeckCards(self):
        return self.commonDeckCards

    def getMyKicker(self):
        return self.getKicker(self.myDeckCards)

    def getCpuKicker(self):
        return self.getKicker(self.cpuDeckCards)

    def getKicker(self, deck):
        numList = []
        for card in deck:
            numList.append(card // 4)
            
        if 0 in numList:
            return 13
        else:
            return max(numList)


        










