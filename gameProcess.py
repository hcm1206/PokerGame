from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
from PIL import ImageTk, Image
from Cards import *
from money import *
from action import GameAction
from CheckJokbo import checkJokbo

class GameProcess:
    def __init__(self, display):
        # self.에 Cards 객체 저장
        self.display = display
        self.CardDeck = Cards()

        

        self.cpuMoneyInfo = MoneyInfo()
        self.myMoneyInfo = MoneyInfo()
        self.Betting = False

        for i in range(5):
            Label(self.display.commonCardFrame, image=self.display.backCard).grid(row=0,column=i)
        for i in range(2):
            Label(self.display.cpuCardFrame, image=self.display.backCard).grid(row=0,column=i)
            Label(self.display.myCardFrame, image=self.display.backCard).grid(row=0,column=i)




# ================================== 게임 진행 부분 ==============================================
    
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
        self.display.cpuMessage.config(text = "", bg=self.display.defaultbg)
        self.display.myMessage.config(text = "", bg=self.display.defaultbg)
        self.display.updateInfo()
        self.CardDeck.initDeck()
        self.display.updateCard()

        for i in range(5):
            Label(self.display.commonCardFrame, image=self.display.backCard).grid(row=0,column=i)
        for i in range(2):
            Label(self.display.cpuCardFrame, image=self.display.backCard).grid(row=0,column=i)
            Label(self.display.myCardFrame, image=self.display.backCard).grid(row=0,column=i)
        self.display.newGameBtn.config(text="게임 시작",command=self.startGame, bg="cyan", fg="black")
    

        

    
    # 게임 시작 (1턴)
    def startGame(self):
        self.turn = 1
        self.Betting = False
        self.cpuMoneyInfo.blind()
        self.myMoneyInfo.blind()
        self.display.updateInfo()

        for i in range(2):
            Label(self.display.myCardFrame, image=self.display.myCards[i]).grid(row=0,column=i)
        self.display.newGameBtn.config(text="새 게임", command=self.confirmRestartGame, bg="yellow")
        self.display.makeButtonsDefault()
        
        

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
                Label(self.display.commonCardFrame, image=self.display.commonCards[i]).grid(row=0,column=i)
        # 현재 3턴 또는 4턴이면 공용카드 1장 공개
        else:
            Label(self.display.commonCardFrame, image=self.display.commonCards[self.turn]).grid(row=0,column=self.turn)

    # 게임 결과 보기 (5턴)
    def resultGame(self):
        self.turn = 5
        self.Betting = False
        self.display.newGameBtn.config(text="결과 정산", command=self.endGame, bg="lime")

        for i in range(2):
            Label(self.display.cpuCardFrame, image=self.display.cpuCards[i]).grid(row=0,column=i)
        self.display.makeButtonsGray()


    def endGame(self):
        myFinalCards = self.CardDeck.getMyDeckCards() + self.CardDeck.getCommonDeckCards()
        cpuFinalCards = self.CardDeck.getCpuDeckCards() + self.CardDeck.getCommonDeckCards()
        myJokbo, self.myScore = checkJokbo(myFinalCards)
        cpuJokbo, self.cpuScore = checkJokbo(cpuFinalCards)
        self.totalBetting = self.cpuMoneyInfo.getTotalBetting() + self.myMoneyInfo.getTotalBetting()
        myKicker = self.CardDeck.getMyKicker()
        cpuKicker = self.CardDeck.getCpuKicker()

        if self.myScore > self.cpuScore:
            self.winGame()
            
        elif self.myScore < self.cpuScore:
            self.loseGame()
            
        else:
            if myKicker > cpuKicker:
                myJokbo += " | 키커 : " + str(self.changeCardNumber(myKicker))
                cpuJokbo += " | 키커 : " + str(self.changeCardNumber(cpuKicker))
                self.winGame()
            elif myKicker < cpuKicker:
                myJokbo += " | 키커 : " + str(self.changeCardNumber(myKicker))
                cpuJokbo += " | 키커 : " + str(self.changeCardNumber(cpuKicker))
                self.loseGame()
            else:
                myJokbo += " | 키커 : " + str(self.changeCardNumber(myKicker))
                cpuJokbo += " | 키커 : " + str(self.changeCardNumber(cpuKicker))
                self.drawGame()

        self.display.myMessage.configure(text = myJokbo)
        self.display.cpuMessage.configure(text = cpuJokbo)
        self.myMoneyInfo.newGame()
        self.cpuMoneyInfo.newGame()
        self.display.updateInfo()
        self.showResult(self.myScore, self.cpuScore, myKicker, cpuKicker, self.totalBetting)
        self.gameSet()
    
    
    def winGame(self):
        self.myMoneyInfo.addMoney(self.totalBetting)
        self.display.myMessage.configure(bg="green")
        self.display.cpuMessage.configure(bg="orange")
    
    def loseGame(self):
        self.cpuMoneyInfo.addMoney(self.totalBetting)
        self.display.myMessage.configure(bg="orange")
        self.display.cpuMessage.configure(bg="green")

    def drawGame(self):
        self.myMoneyInfo.addMoney(self.totalBetting//2)
        self.cpuMoneyInfo.addMoney(self.totalBetting//2)
        self.display.myMessage.configure(bg="orange")
        self.display.cpuMessage.configure(bg="orange")


    def changeCardNumber(self, num):

        numList = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        return numList[num]
        
    
    def showResult(self, myScore, cpuScore, myKicker, cpuKicker, totalBetting):
        if (myScore > cpuScore) or ((myScore == cpuScore) and (myKicker > cpuKicker)):
            tkinter.messagebox.showinfo("판돈 확보 성공", str(totalBetting) + "을 획득하였습니다.")
        elif (myScore < cpuScore) or ((myScore == cpuScore) and (myKicker < cpuKicker)):
            tkinter.messagebox.showinfo("핀돈 확보 실패", "상대방이 " + str(totalBetting) + "을 가져갑니다.")
        else:
            tkinter.messagebox.showinfo("무승부", "판돈의 절반 " + str(totalBetting//2) + "을 획득하였습니다.")


    def gameSet(self):
        if self.myMoneyInfo.getMoney() <= 0:
            tkinter.messagebox.showinfo("파산", "소지 금액을 모두 잃었으므로 게임에서 패배하였습니다.")
            self.display.newGameBtn.config(text="게임 초기화", command=self.confirmInitMoney, bg="red", fg="white")
        elif self.cpuMoneyInfo.getMoney() <= 0:
            tkinter.messagebox.showinfo("승리", "상대방의 소지 금액이 모두 소진되어 게임에서 승리하였습니다.")
            self.display.newGameBtn.config(text="게임 초기화", command=self.confirmInitMoney, bg="red", fg="white")
        else:
            self.display.newGameBtn.config(text="새 게임", command=self.confirmInitGame, bg="yellow")



    
    def initMoney(self):
        self.myMoneyInfo.initMoney()
        self.cpuMoneyInfo.initMoney()
        self.initGame()
    
    def confirmInitMoney(self):
        initGame = tkinter.messagebox.askokcancel("게임 초기화", "현재 게임 진행 및 잔금을 초기화하시겠습니까?")
        if initGame:
            self.initMoney()



    # 블라인드 설정하는 메소드
    # 최소 블라인드와 최대 블라인드 적용 기준은 어떻게 해야 할지 토의 필요
    def settingBlind(self):
        while(1):
            newBlind = tkinter.simpledialog.askinteger("블라인드 설정", "설정할 블라인드 액수를 입력하세요")
            try:
                if int(newBlind) < 100:
                    tkinter.messagebox.showwarning("알림", "설정 가능한 블라인드의 최소액은 100입니다.")
                    continue
                elif int(newBlind) > 5000:
                    tkinter.messagebox.showwarning("알림", "설정 가능한 블라인드의 최대액은 5000입니다.")
                    continue
                else:
                    confirmBetting = tkinter.messagebox.askokcancel("블라인드 설정", "블라인드로 " + str(newBlind) + "을 설정하시겠습니까?")
                    if confirmBetting:
                        break
                    else:
                        continue
            except:
                return
        self.cpuMoneyInfo.setBlind(newBlind)
        self.myMoneyInfo.setBlind(newBlind)
        self.display.updateInfo()
        if self.turn != 0:
            tkinter.messagebox.showinfo("알림", "다음 게임부터 " + str(newBlind) + "의 블라인드가 적용됩니다.")