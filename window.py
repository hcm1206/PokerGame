from tkinter import *
from PIL import ImageTk, Image
import random
from Cards import Cards

class Display:
    def __init__(self):
        window = Tk()
        window.title("Poker Game")

        # 카드 이미지 크기 설정
        self.height = 110
        self.width = 80
        

        # self.에 Cards 객체 저장
        self.CardDeck = Cards()

        # 게임 창의 각 프레임 구성
        self.cpuInfoFrame = Frame(window)
        self.cpuCardFrame = Frame(window)
        self.commonCardFrame = Frame(window)
        self.myCardFrame = Frame(window)
        self.buttonFrame = Frame(window)

        newGameBtn = Button(self.buttonFrame, text="새 게임", command=self.initGame)
        newGameBtn.grid(row=0,column=0)
        battingBtn = Button(self.buttonFrame, text="배팅하기")
        battingBtn.grid(row=0,column=1)

        # 게임 창의 각 프레임 출력
        self.cpuInfoFrame.pack()
        self.cpuCardFrame.pack()
        self.commonCardFrame.pack()
        self.myCardFrame.pack()
        self.buttonFrame.pack()

        self.backCard = self.displayBackCard()



        # 게임 초기 설정
        self.initGame()

        # 이미지 객체가 저장된 리스트 만들기
        self.myCards = self.displayCardofDeck(self.CardDeck.drawMyCard())
        self.cpuCards = self.displayCardofDeck(self.CardDeck.drawCpuCard())
        self.commonCards = self.displayCardofDeck(self.CardDeck.drawInitCommonCard())

        window.mainloop()

    # 숫자 리스트를 입력하면 카드 이미지 객체 리스트로 변환
    def displayCardofDeck(self, deck):
        cards = []
        for card in deck:
            cards.append(self.displayCard(card))
        return cards

    # 숫자를 입력하면 카드 이미지 객체로 변환
    def displayCard(self, num):
        card = Image.open("card\d"+str(num)+".png")
        card = card.resize((self.width, self.height))
        card = ImageTk.PhotoImage(card)
        return card

    # 카드 뒷면 이미지 객체 받아오는 메소드
    def displayBackCard(self):
        backCard = Image.open("card\dback.png")
        backCard = backCard.resize((self.width, self.height))
        backCard = ImageTk.PhotoImage(backCard)
        return backCard


    # 게임 초기화 및 재시작 (0턴으로 돌리기)
    def initGame(self):
        self.turn = 0
        self.CardDeck.index = 0
        self.CardDeck.shuffleDeck()
        self.myCards = self.displayCardofDeck(self.CardDeck.drawMyCard())
        self.cpuCards = self.displayCardofDeck(self.CardDeck.drawCpuCard())
        self.commonCards = self.displayCardofDeck(self.CardDeck.drawInitCommonCard())
        for i in range(5):
            Label(self.commonCardFrame, image=self.backCard).grid(row=0,column=i)
        for i in range(2):
            Label(self.cpuCardFrame, image=self.backCard).grid(row=0,column=i)
            Label(self.myCardFrame, image=self.backCard).grid(row=0,column=i)
        self.nextBtn = Button(self.buttonFrame, text="게임 시작", command=self.startGame)
        self.nextBtn.grid(row=0,column=2)
    
    def startGame(self):
        self.turn = 1
        self.nextBtn = Button(self.buttonFrame, text="다음 진행", command=self.nextGame)
        self.nextBtn.grid(row=0,column=2)
        for i in range(2):
            Label(self.myCardFrame, image=self.myCards[i]).grid(row=0,column=i)
        for i in range(3):
            Label(self.commonCardFrame, image=self.commonCards[i]).grid(row=0,column=i)

    def nextGame(self):
        self.turn += 1
        Label(self.commonCardFrame, image=self.commonCards[self.turn+1]).grid(row=0,column=self.turn+1)
        if self.turn >= 3:
            self.resultBtn = Button(self.buttonFrame, text="결과 보기", command=self.resultGame)
            self.resultBtn.grid(row=0,column=2)

    def resultGame(self):
        newGameBtn = Button(self.buttonFrame, text="게임 종료", command=self.quitGame)
        newGameBtn.grid(row=0,column=2)
        for i in range(2):
            Label(self.cpuCardFrame, image=self.cpuCards[i]).grid(row=0,column=i)

    def quitGame(self):
        exit(0)


