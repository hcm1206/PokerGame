from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
from PIL import ImageTk, Image
from Cards import *
from money import *

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

        self.cpuMoneyInfo = MoneyInfo()
        self.myMoneyInfo = MoneyInfo()
        self.Betting = False



        # UI에 표시할 정보
        self.yourMoney = 10000
        self.cpuMoney = 10000
        self.Betting = 0

        # 게임 창의 각 프레임 구성
        self.cpuInfoFrame = Frame(window)
        self.cpuCardFrame = Frame(window)
        self.commonCardFrame = Frame(window)
        self.myCardFrame = Frame(window)
        self.buttonFrame = Frame(window)
        self.myInfoFrame = Frame(window)

        
        

        # 버튼 생성
        foldBtn = Button(self.buttonFrame, text="폴드", command=self.confirmFoldGame)
        foldBtn.grid(row=0,column=1)
        BettingBtn = Button(self.buttonFrame, text="배팅하기", command=self.BettingMoney)
        BettingBtn.grid(row=0,column=2)
        foldBtn = Button(self.buttonFrame, text="체크", command=self.confirmCheckGame)
        foldBtn.grid(row=0,column=3)
        foldBtn = Button(self.buttonFrame, text="올인", command=self.confirmAllInGame)
        foldBtn.grid(row=0,column=4)
        newGameBtn = Button(self.buttonFrame, text="게임 종료", command=self.confirmQuitGame)
        newGameBtn.grid(row=0,column=5)
        
        
        self.updateInfo()
        

        # 게임 창의 각 프레임 출력
        self.cpuInfoFrame.pack()
        self.cpuCardFrame.pack()
        self.commonCardFrame.pack()
        self.myCardFrame.pack()
        self.buttonFrame.pack()
        self.myInfoFrame.pack()

        self.backCard = self.displayBackCard()

        

        

        # 이미지 객체가 저장된 리스트 만들기
        self.myCards = self.displayCardofDeck(self.CardDeck.drawMyCard())
        self.cpuCards = self.displayCardofDeck(self.CardDeck.drawCpuCard())
        self.commonCards = self.displayCardofDeck(self.CardDeck.drawInitCommonCard())

        # 게임 초기 설정
        self.initGame()

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
        gameQuit = tkinter.messagebox.askokcancel("새로운 게임 시작", "게임을 새로 시작하시겠습니까?")
        if gameQuit:
            self.initGame()

    def confirmRestartGame(self):
        gameRestart = tkinter.messagebox.askokcancel("게임 재시작", "게임을 재시작 하시겠습니까?")
        if gameRestart:
            self.cpuMoneyInfo.addMoney(self.cpuMoneyInfo.getTotalBetting())
            self.myMoneyInfo.addMoney(self.myMoneyInfo.getTotalBetting())
            self.initGame()

    # 게임 초기화 (0턴으로 돌리기)
    def initGame(self):
        self.turn = 0
        self.myMoneyInfo.newGame()
        self.cpuMoneyInfo.newGame()
        self.updateInfo()
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
        newGameBtn = Button(self.buttonFrame, text="게임 시작", command=self.startGame, width=8, bg="cyan")
        newGameBtn.grid(row=0,column=0)
    

        

    
    # 게임 시작 (1턴)
    def startGame(self):
        self.turn = 1
        self.Betting = False
        self.cpuMoneyInfo.blind()
        self.myMoneyInfo.blind()
        self.updateInfo()
        for i in range(2):
            Label(self.myCardFrame, image=self.myCards[i]).grid(row=0,column=i)
        Button(self.buttonFrame, text="새 게임", command=self.confirmRestartGame, width=8, bg="yellow").grid(row=0,column=0)
        
        

    # 게임 진행 (2턴~4턴)
    def nextGame(self):
        if self.Betting == False:
            tkinter.messagebox.showwarning("알림", "배팅 또는 폴드를 진행해주세요.")
            return
        self.turn += 1
        self.Betting = False
        # 현재 2턴이면 공용카드 3장 공개
        if self.turn == 2:
            for i in range(3):
                Label(self.commonCardFrame, image=self.commonCards[i]).grid(row=0,column=i)
        # 현재 3턴 또는 4턴이면 공용카드 1장 공개
        else:
            Label(self.commonCardFrame, image=self.commonCards[self.turn]).grid(row=0,column=self.turn)
        if self.turn >= 4:
            Button(self.buttonFrame, text="결과 보기", command=self.resultGame, width=8, bg="lime").grid(row=0,column=0)

    # 게임 결과 보기 (5턴)
    def resultGame(self):
        self.turn = 5
        self.Betting = False
        Button(self.buttonFrame, text="결과 정산", command=self.endGame, width=8, bg="lime").grid(row=0,column=0)
        for i in range(2):
            Label(self.cpuCardFrame, image=self.cpuCards[i]).grid(row=0,column=i)

    def foldGame(self):
        self.turn = 5
        for i in range(5):
            Label(self.commonCardFrame, image=self.commonCards[i]).grid(row=0,column=i)
        for i in range(2):
            Label(self.cpuCardFrame, image=self.cpuCards[i]).grid(row=0,column=i)
        Button(self.buttonFrame, text="결과 정산", command=self.endGame, width=8, bg="lime").grid(row=0,column=0)

    def confirmFoldGame(self):
        if (1 > self.turn or self.turn > 4):
            tkinter.messagebox.showwarning("알림", "게임 진행 중에만 폴드가 가능합니다.")
            return
        gameQuit = tkinter.messagebox.askokcancel("폴드", "이번 게임을 폴드하시겠습니까?")
        if gameQuit:
            self.foldGame()

    def AllInGame(self):
        self.turn = 5
        self.myMoneyInfo.allIn()
        self.cpuMoneyInfo.allIn()
        self.updateInfo()
        self.Betting = True
        for i in range(5):
            Label(self.commonCardFrame, image=self.commonCards[i]).grid(row=0,column=i)
        for i in range(2):
            Label(self.cpuCardFrame, image=self.cpuCards[i]).grid(row=0,column=i)
        Button(self.buttonFrame, text="결과 정산", command=self.endGame, width=8, bg="lime").grid(row=0,column=0)

    def confirmAllInGame(self):
        if (1 > self.turn or self.turn > 4):
            tkinter.messagebox.showwarning("알림", "게임 진행 중에만 올인이 가능합니다.")
            return
        gameQuit = tkinter.messagebox.askokcancel("올인", "이번 게임에 올인하시겠습니까?")
        if gameQuit:
            self.AllInGame()

    # 게임 종료 커맨드
    def quitGame(self):
        exit(0)

    # 게임 종료 전 사용자에게 게임 종료 여부 묻기
    def confirmQuitGame(self):
        gameQuit = tkinter.messagebox.askokcancel("게임 종료", "정말 게임을 종료하시겠습니까?")
        if gameQuit:
            self.quitGame()

    def endGame(self):
        totalBetting = self.cpuMoneyInfo.getTotalBetting() + self.myMoneyInfo.getTotalBetting()
        self.myMoneyInfo.addMoney(totalBetting)
        self.myMoneyInfo.newGame()
        self.cpuMoneyInfo.newGame()
        self.updateInfo()
        tkinter.messagebox.showinfo("게임 승리", str(totalBetting) + "을 획득하였습니다.")
        Button(self.buttonFrame, text="새 게임", command=self.confirmInitGame, width=8, bg="yellow").grid(row=0,column=0)
    


    def BettingMoney(self):
        if 1 > self.turn or self.turn > 4:
            tkinter.messagebox.showwarning("알림", "게임 진행 중에만 배팅이 가능합니다.")
            return
        while(1):
            BettingAmount = tkinter.simpledialog.askinteger("배팅액 입력", "배팅액을 입력하세요")
            try:
                if int(BettingAmount) < self.myMoneyInfo.getMinimumBetting():
                    tkinter.messagebox.showwarning("알림", "최소 " + str(self.myMoneyInfo.getMinimumBetting()) + "이상 배팅하셔야 합니다.")
                    print(BettingAmount)
                    continue
                elif BettingAmount == self.myMoneyInfo.getMoney():
                    self.confirmAllInGame()
                    return
                elif int(BettingAmount) > self.myMoneyInfo.getMoney():
                    tkinter.messagebox.showwarning("알림", "현재 소지 금액을 초과하였습니다.")
                    continue
                else:
                    confirmBetting = tkinter.messagebox.askokcancel("배팅", str(BettingAmount) + "을 배팅하시겠습니까?")
                    if confirmBetting:
                        break
                    else:
                        continue
            except:
                return
        
        self.myMoneyInfo.addBetting(BettingAmount)
        self.cpuMoneyInfo.addBetting(BettingAmount)
        self.updateInfo()
        self.Betting = True
        self.nextGame()

    def checkGame(self):
        self.myMoneyInfo.addBetting(self.myMoneyInfo.getMinimumBetting())
        self.cpuMoneyInfo.addBetting(self.cpuMoneyInfo.getMinimumBetting())
        self.updateInfo()
        self.Betting = True
        self.nextGame()
    
    def confirmCheckGame(self):
        if (1 > self.turn or self.turn > 4):
            tkinter.messagebox.showwarning("알림", "게임 진행 중에만 체크가 가능합니다.")
            return
        gameQuit = tkinter.messagebox.askokcancel("체크", "체크하시겠습니까?")
        if gameQuit:
            self.checkGame()



    def updateInfo(self):
        # CPU의 정보 창
        self.cpuMoney = Label(self.cpuInfoFrame, text="상대의 총액 : " + str(self.cpuMoneyInfo.getMoney()), width=20)
        self.cpuBetting = Label(self.cpuInfoFrame, text="상대의 배팅액 : " + str(self.cpuMoneyInfo.getTotalBetting()), width=20)
        self.cpuMoney.grid(row=0,column=0)
        self.cpuBetting.grid(row=0,column=1)
        # 사용자의 정보 창
        self.myMoney = Label(self.myInfoFrame, text="당신의 총액 : " + str(self.myMoneyInfo.getMoney()), width=20)
        self.minimumBetting = Label(self.myInfoFrame, text="최소 배팅액 : " + str(self.myMoneyInfo.getMinimumBetting()), width=20)
        self.myBetting = Label(self.myInfoFrame, text="당신의 배팅액 : " + str(self.myMoneyInfo.getTotalBetting()), width=20)
        self.myMoney.grid(row=0,column=0)
        self.minimumBetting.grid(row=0,column=1)
        self.myBetting.grid(row=0,column=2)

    



