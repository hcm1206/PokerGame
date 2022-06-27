from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Cards import *

# 화면에 GUI로 표시할 내용이 포함된 클래스

class Display:
    def __init__(self):
        window = Tk()
        window.title("Poker Game")

        # 카드 이미지 크기 설정
        self.height = 110
        self.width = 80
        
        # self.에 Cards 객체 저장
        self.CardDeck = Cards()

        # UI에 표시할 정보
        self.yourMoney = 10000
        self.cpuMoney = 10000
        self.batting = 0

        # 게임 창의 각 프레임 구성
        self.cpuInfoFrame = Frame(window)
        self.cpuCardFrame = Frame(window)
        self.commonCardFrame = Frame(window)
        self.myCardFrame = Frame(window)
        self.buttonFrame = Frame(window)

        # 정보 창 출력
        cpuMoneyInfo = Label(self.cpuInfoFrame, text="CPU Money : " + str(self.cpuMoney), width=20)
        battingInfo = Label(self.cpuInfoFrame, text="Batting : " + str(self.batting), width=20)
        yourMoneyInfo = Label(self.cpuInfoFrame, text="Your Money : " + str(self.yourMoney), width=20)
        cpuMoneyInfo.grid(row=0,column=0)
        battingInfo.grid(row=0,column=2)
        yourMoneyInfo.grid(row=0,column=4)

        # 버튼 2개 생성
        newGameBtn = Button(self.buttonFrame, text="새 게임", command=self.confirmInitGame)
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

    
    # 게임 진행은 총 6개의 턴으로 구분 (0턴~5턴)
    # 0턴 : 게임 준비 상태 (모든 카드 비공개 상태)
    # 1턴 : 게임 시작 (본인 카드 2장 공개 및 배팅 시작)
    # 2턴 : 게임 진행 (공용 카드 3장 공개(3/5) 및 배팅)
    # 3턴 : 게임 진행 (공용 카드 1장 공개(4/5) 및 배팅)
    # 4턴 : 게임 진행 (공용 카드 1장 공개(5/5) 및 최종 배팅)
    # 5턴 : 게임 종료 (모든 카드 공개 및 결과 정산)

    # 게임 재시작 전 사용자에게 게임 재시작 여부 묻기
    def confirmInitGame(self):
        gameQuit = messagebox.askokcancel("게임 재시작", "게임을 새로 시작하시겠습니까?")
        if gameQuit:
            self.initGame()


    # 게임 초기화 (0턴으로 돌리기)
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
    
    # 게임 시작 (1턴)
    def startGame(self):
        self.turn = 1
        self.nextBtn = Button(self.buttonFrame, text="다음 진행", command=self.nextGame)
        self.nextBtn.grid(row=0,column=2)
        for i in range(2):
            Label(self.myCardFrame, image=self.myCards[i]).grid(row=0,column=i)
        

    # 게임 진행 (2턴~4턴)
    def nextGame(self):
        self.turn += 1
        # 현재 2턴이면 공용카드 3장 공개
        if self.turn == 2:
            for i in range(3):
                Label(self.commonCardFrame, image=self.commonCards[i]).grid(row=0,column=i)
        # 현재 3턴 또는 4턴이면 공용카드 1장 공개
        else:
            Label(self.commonCardFrame, image=self.commonCards[self.turn]).grid(row=0,column=self.turn)
        if self.turn >= 4:
            self.resultBtn = Button(self.buttonFrame, text="결과 보기", command=self.resultGame)
            self.resultBtn.grid(row=0,column=2)

    # 게임 결과 보기 (5턴)
    def resultGame(self):
        newGameBtn = Button(self.buttonFrame, text="게임 종료", command=self.confirmQuitGame)
        newGameBtn.grid(row=0,column=2)
        for i in range(2):
            Label(self.cpuCardFrame, image=self.cpuCards[i]).grid(row=0,column=i)

    # 게임 종료 커맨드
    def quitGame(self):
        exit(0)

    # 게임 종료 전 사용자에게 게임 종료 여부 묻기
    def confirmQuitGame(self):
        gameQuit = messagebox.askokcancel("게임 종료", "정말 게임을 종료하시겠습니까?")
        if gameQuit:
            self.quitGame()


