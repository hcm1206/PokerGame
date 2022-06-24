import random

from sqlalchemy import true

# 카드 덱 리스트의 숫자를 처리하는 클래스
class Cards():
    # 52개의 카드 숫자 덱 리스트 생성
    def __init__(self):
        self.deck = [x for x in range(52)]
        self.index = 0

    # 카드 덱의 숫자 섞기
    def shuffleDeck(self):
        random.shuffle(self.deck)


    # 아래는 실제로 사용될 코드, 테스트 코드 삭제 후 주석 해제

    # 유저의 최초 카드 2장의 숫자를 덱에서 뽑아서 결정
    def drawMyCard(self):
        myCard = []
        for i in range(self.index,self.index+2):
            myCard.append(self.deck[i])
        self.index += 2
        return myCard

    # 상대방의 최초 카드 2장의 숫자를 덱에서 뽑아서 결정
    def drawCpuCard(self):
        cpuCard = []
        for i in range(self.index,self.index+2):
            cpuCard.append(self.deck[i])
        self.index += 2
        return cpuCard
    
    # 최초 공용카드 5장의 숫자를 덱에서 뽑아서 결정
    def drawInitCommonCard(self):
        commonCard = []
        for i in range(self.index,self.index+3):
            commonCard.append(self.deck[i])
        self.index += 3
        return commonCard
        

    # # 이 아래로는 테스트용 코드, 테스트 이후 지울 것 ===================================================

    # # 유저의 카드 5장의 숫자를 덱에서 뽑아서 결정
    # def drawMyCard(self):
    #     myCard = []
    #     for i in range(5):
    #         myCard.append(self.deck[i])
    #     return myCard

    # # 상대방의 카드 5장의 숫자를 덱에서 뽑아서 결정
    # def drawCpuCard(self):
    #     cpuCard = []
    #     for i in range(5,10):
    #         cpuCard.append(self.deck[i])
    #     return cpuCard
    
    # # 최초 공용카드 5장의 숫자를 덱에서 뽑아서 결정
    # def drawCommonCard(self):
    #     commonCard = []
    #     for i in range(10,15):
    #         commonCard.append(self.deck[i])
    #     return commonCard

    # # 테스트 코드 종료 지점 ========================================================








