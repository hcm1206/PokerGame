from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
from PIL import ImageTk, Image
from Cards import *
from money import *
from action import GameAction
from CheckJokbo import checkJokbo
from gameProcess import GameProcess

# 화면에 GUI로 표시할 내용이 포함된 클래스

class Display:
    def __init__(self):

        

        window = Tk()
        window.title("Poker Game")

        mainMenu = Menu(window)
        window.configure(menu = mainMenu)

        subMenu = Menu(mainMenu, tearoff=0)

        


        

        # 카드 이미지 크기 설정
        self.height = 110
        self.width = 80
        

        self.backCard = self.displayBackCard()



        # 게임 창의 각 프레임 구성
        self.cpuInfoFrame = Frame(window)
        self.cpuMessageFrame = Frame(window)
        self.cpuCardFrame = Frame(window)
        self.commonCardFrame = Frame(window)
        self.myCardFrame = Frame(window)
        self.myMessageFrame = Frame(window)
        self.buttonFrame = Frame(window)
        self.myInfoFrame = Frame(window)

        self.cpuMessage = Label(self.cpuMessageFrame, text="", height=2)
        self.myMessage = Label(self.myMessageFrame, text="", height=2)
        self.cpuMessage.pack()
        self.myMessage.pack()

        self.game = GameProcess(self)

        mainMenu.add_cascade(label="게임 설정", menu=subMenu)
        subMenu.add_command(label="게임 초기화", command=self.game.confirmInitMoney)
        subMenu.add_command(label="블라인드 설정", command=self.game.settingBlind)

        # CPU의 정보 창
        self.cpuMoney = Label(self.cpuInfoFrame, text="상대의 총액 : " + str(self.game.cpuMoneyInfo.getMoney()), width=20)
        self.cpuBetting = Label(self.cpuInfoFrame, text="상대의 배팅액 : " + str(self.game.cpuMoneyInfo.getTotalBetting()), width=20)
        self.cpuMoney.grid(row=0,column=0)
        self.cpuBetting.grid(row=0,column=1)
        # 사용자의 정보 창
        self.myMoney = Label(self.myInfoFrame, text="당신의 총액 : " + str(self.game.myMoneyInfo.getMoney()), width=20)
        self.nowBlind = Label(self.myInfoFrame, text="블라인드 : " + str(self.game.myMoneyInfo.getBlindAmount()), width=20)
        self.myBetting = Label(self.myInfoFrame, text="당신의 배팅액 : " + str(self.game.myMoneyInfo.getTotalBetting()), width=20)
        self.myMoney.grid(row=0,column=0)
        self.nowBlind.grid(row=0,column=1)
        self.myBetting.grid(row=0,column=2)

        
        
        # 버튼 생성
        self.newGameBtn = Button(self.buttonFrame, text="게임 시작", command=self.game.startGame, width=8, bg="cyan")
        self.newGameBtn.grid(row=0,column=0)
        self.foldBtn = Button(self.buttonFrame, text="폴드", bg="lightgray", command=GameAction(self).confirmFoldGame)
        self.foldBtn.grid(row=0,column=1)
        self.BettingBtn = Button(self.buttonFrame, text="배팅", bg="lightgray", command=GameAction(self).BettingMoney)
        self.BettingBtn.grid(row=0,column=2)
        self.checkBtn = Button(self.buttonFrame, text="체크", bg="lightgray", command=GameAction(self).confirmCheckGame)
        self.checkBtn.grid(row=0,column=3)
        self.AllInBtn = Button(self.buttonFrame, text="올인", bg="lightgray", command=GameAction(self).confirmAllInGame)
        self.AllInBtn.grid(row=0,column=4)
        self.QuitGameBtn = Button(self.buttonFrame, text="게임 종료", bg="gray", command=GameAction(self).confirmQuitGame)
        self.QuitGameBtn.grid(row=0,column=5)

        # 기본 UI 배경색 설정
        self.defaultbg = self.cpuInfoFrame.cget('bg')
        
        
        self.updateInfo()
        

        # 게임 창의 각 프레임 출력
        self.cpuInfoFrame.pack()
        self.cpuMessageFrame.pack()
        self.cpuCardFrame.pack()
        self.commonCardFrame.pack()
        self.myCardFrame.pack()
        self.myMessageFrame.pack()
        self.buttonFrame.pack()
        self.myInfoFrame.pack()

        

    

        # 이미지 객체가 저장된 리스트 만들기
        self.updateCard()

        

        # UI 실행
        window.mainloop()

    # 현재 카드덱에 맞는 이미지 파일 불러오기
    def updateCard(self):
        self.myCards = self.displayCardofDeck(self.game.CardDeck.drawMyCard())
        self.cpuCards = self.displayCardofDeck(self.game.CardDeck.drawCpuCard())
        self.commonCards = self.displayCardofDeck(self.game.CardDeck.drawInitCommonCard())

        

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


    # 액션 버튼 색깔 회색으로 바꾸기
    def makeButtonsGray(self):
        self.foldBtn.config(bg="lightgray")
        self.BettingBtn.config(bg="lightgray")
        self.checkBtn.config(bg="lightgray")
        self.AllInBtn.config(bg="lightgray")

    # 액션 버튼 색깔 기본값으로 바꾸기
    def makeButtonsDefault(self):
        self.foldBtn.config(bg=self.defaultbg)
        self.BettingBtn.config(bg=self.defaultbg)
        self.checkBtn.config(bg=self.defaultbg)
        self.AllInBtn.config(bg=self.defaultbg)

        

    # UI 텍스트 정보 갱신
    def updateInfo(self):
        # CPU의 정보 창
        self.cpuMoney.config(text="상대의 총액 : " + str(self.game.cpuMoneyInfo.getMoney()))
        self.cpuBetting.config(text="상대의 배팅액 : " + str(self.game.cpuMoneyInfo.getTotalBetting()))
        # 사용자의 정보 창
        self.myMoney.config(text="당신의 총액 : " + str(self.game.myMoneyInfo.getMoney()))
        self.myBetting.config(text="당신의 배팅액 : " + str(self.game.myMoneyInfo.getTotalBetting()))
        self.nowBlind.config(text="블라인드 : " + str(self.game.myMoneyInfo.getBlindAmount()))



    

    

        


