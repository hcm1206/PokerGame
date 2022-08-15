from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
from CheckJokbo import checkJokbo, getKicker

class GameAction:
    def __init__(self, window):
        self.window = window
        self.PlayerFold = True
    
    def playerFoldGame(self):
        self.PlayerFold = True
        self.foldGame()

    def cpuFoldGame(self):
        self.PlayerFold = False
        tkinter.messagebox.showinfo("폴드", "상대방이 폴드를 선언했습니다.")
        self.foldGame()

    # 사용자가 폴드 했을 때 실행되는 코드
    def foldGame(self):
        self.window.game.turn = 5
        for i in range(5):
            newImage = self.window.commonCards[i]
            self.window.commonCardImgs[i].config(image=newImage)
            self.window.commonCardImgs[i].image = newImage
        for i in range(2):
            newImage = self.window.cpuCards[i]
            self.window.cpuCardImgs[i].config(image=newImage)
            self.window.cpuCardImgs[i].image = newImage
        self.window.newGameBtn.config(text="결과 보기", command=self.foldGameResult, bg="lime")
        self.window.makeButtonsGray()

    # 폴드 후 결과 출력하기
    def foldGameResult(self):
        myFinalCards = self.window.game.CardDeck.getMyDeckCards() + self.window.game.CardDeck.getCommonDeckCards()
        cpuFinalCards = self.window.game.CardDeck.getCpuDeckCards() + self.window.game.CardDeck.getCommonDeckCards()
        myJokbo, myScore = checkJokbo(myFinalCards)
        cpuJokbo, cpuScore = checkJokbo(cpuFinalCards)
        if myScore == cpuScore:
            myKicker = getKicker(self.window.game.CardDeck.getMyDeckCards(), myScore)
            cpuKicker = getKicker(self.window.game.CardDeck.getCpuDeckCards(), cpuScore)
            myJokbo += " | 키커 : " + str(self.window.game.changeCardNumber(myKicker))
            cpuJokbo += " | 키커 : " + str(self.window.game.changeCardNumber(cpuKicker))
        self.window.myMessage.configure(text = myJokbo)
        self.window.cpuMessage.configure(text = cpuJokbo)
        self.totalBetting = self.window.game.cpuMoneyInfo.getTotalBetting() + self.window.game.myMoneyInfo.getTotalBetting()
        if self.PlayerFold:
            self.window.game.cpuMoneyInfo.addMoney(self.totalBetting)
            self.window.game.myMoneyInfo.newGame()
            self.window.game.cpuMoneyInfo.newGame()
            self.window.updateInfo()
            tkinter.messagebox.showinfo("폴드", "상대방이 " + str(self.totalBetting) + "을 가져갑니다.")
            self.window.game.gameSet()
        else:
            self.window.game.myMoneyInfo.addMoney(self.totalBetting)
            self.window.game.myMoneyInfo.newGame()
            self.window.game.cpuMoneyInfo.newGame()
            self.window.updateInfo()
            tkinter.messagebox.showinfo("폴드", "당신이 " + str(self.totalBetting) + "을 가져갑니다.")
            self.window.game.gameSet()

    # 현재 폴드가 가능한지 확인 후 사용자에게 정말로 폴드할 것인지 재확인
    def confirmFoldGame(self):
        if (1 > self.window.game.turn or self.window.game.turn > 4):
            tkinter.messagebox.showwarning("알림", "게임 진행 중에만 폴드가 가능합니다.")
            return
        foldGame = tkinter.messagebox.askokcancel("폴드", "이번 게임을 폴드하시겠습니까?")
        if foldGame:
            self.playerFoldGame()

    # 사용자가 올인했을 때 실행되는 코드
    def AllInGame(self):
        if self.window.game.AI.allInReply():
            self.window.game.turn = 5
            self.window.game.myMoneyInfo.allIn(self.window.game.cpuMoneyInfo)
            # self.window.game.cpuMoneyInfo.allIn()
            self.window.updateInfo()
            self.window.game.Betting = True
            for i in range(5):
                newImage = self.window.commonCards[i]
                self.window.commonCardImgs[i].config(image=newImage)
                self.window.commonCardImgs[i].image = newImage
            for i in range(2):
                newImage = self.window.cpuCards[i]
                self.window.cpuCardImgs[i].config(image=newImage)
                self.window.cpuCardImgs[i].image = newImage
            self.window.newGameBtn.config(text="결과 정산", command=self.window.game.endGame, bg="lime")
            self.window.makeButtonsGray()
        else:
            self.cpuFoldGame()


    # 현재 올인이 가능한지 확인 후 사용자에게 정말 올인할 것인지 재확인
    def confirmAllInGame(self):
        if (1 > self.window.game.turn or self.window.game.turn > 4):
            tkinter.messagebox.showwarning("알림", "게임 진행 중에만 올인이 가능합니다.")
            return
        allInGame = tkinter.messagebox.askokcancel("올인", "이번 게임에 올인하시겠습니까?")
        if allInGame:
            self.AllInGame()

    # 게임 종료 커맨드
    def quitGame(self):
        exit(0)

    # 게임 종료 전 사용자에게 게임 종료 여부 묻기
    def confirmQuitGame(self):
        gameQuit = tkinter.messagebox.askokcancel("게임 종료", "정말 게임을 종료하시겠습니까?")
        if gameQuit:
            self.quitGame()


    

    # 현재 베팅이 가능한지 확인 후 사용자에게 알맞은 베팅 값을 입력받아 베팅 진행
    def BettingMoney(self):
        if 1 > self.window.game.turn or self.window.game.turn > 4:
            tkinter.messagebox.showwarning("알림", "게임 진행 중에만 베팅이 가능합니다.")
            return
        # 사용자가 알맞은 베팅팅액을 입력할 때까지 무한 루프
        while(1):
            BettingAmount = tkinter.simpledialog.askinteger("베팅액 입력", "베팅액을 입력하세요")
            try:
                if int(BettingAmount) < self.window.game.myMoneyInfo.getMinimumBetting():
                    tkinter.messagebox.showwarning("알림", "최소 " + str(self.window.game.myMoneyInfo.getMinimumBetting()) + "이상 베팅하셔야 합니다.")
                    continue
                elif BettingAmount == 0:
                    self.confirmCheckGame()
                    return
                elif BettingAmount == self.window.game.myMoneyInfo.getMoney():
                    self.confirmAllInGame()
                    return
                elif int(BettingAmount) > self.window.game.myMoneyInfo.getMoney():
                    tkinter.messagebox.showwarning("알림", "현재 소지 금액을 초과하였습니다.")
                    continue
                else:
                    confirmBetting = tkinter.messagebox.askokcancel("베팅", str(BettingAmount) + "을 베팅하시겠습니까?")
                    if confirmBetting:
                        break
                    else:
                        continue
            except:
                return

        if self.window.game.AI.bettingReply(BettingAmount):
            self.window.game.myMoneyInfo.addBetting(BettingAmount)
            if self.window.game.cpuMoneyInfo.getMoney() >= BettingAmount:
                self.window.game.cpuMoneyInfo.addBetting(BettingAmount)
            else:
                self.window.game.cpuMoneyInfo.addBetting(self.window.game.cpuMoneyInfo.getMoney())
            self.window.updateInfo()
            self.window.game.Betting = True
            if self.window.game.turn >= 4:
                self.window.newGameBtn.config(text="결과 보기", command=self.window.game.resultGame, bg="lime")
                self.window.makeButtonsGray()
                self.window.game.turn = 5
                return
            self.window.game.nextGame()
        else:
            self.cpuFoldGame()

    # 사용자가 체크시 실행할 코드
    def checkGame(self):
        if self.window.game.myMoneyInfo.getMinimumBetting():
            tkinter.messagebox.showwarning("알림", "최소 " + str(self.window.game.myMoneyInfo.getMinimumBetting()) + "이상 베팅하셔야 합니다.")
            return
        AIBetting = self.window.game.AI.whetherBetting()
        if not AIBetting:
            self.window.game.Betting = True
            if self.window.game.turn >= 4:
                self.window.newGameBtn.config(text="결과 보기", command=self.window.game.resultGame, bg="lime")
                self.window.makeButtonsGray()
                self.window.game.turn = 5
                return
            self.window.game.nextGame()
        else:
            self.window.game.myMoneyInfo.setMinimumBetting(AIBetting)
            if self.window.game.cpuMoneyInfo.getMoney() > AIBetting:
                tkinter.messagebox.showinfo("베팅", "상대방이 " + str(AIBetting) + "을 베팅했습니다.")
                self.window.updateInfo()
            else:
                self.cpuAllInGame()
                

    def cpuAllInGame(self):
        tkinter.messagebox.showinfo("올인", "상대방이 올인했습니다.")
        replyAllIn = tkinter.messagebox.askokcancel("올인", "상대의 올인에 대응하여 베팅하시겠습니까?")
        if replyAllIn:
            self.window.game.turn = 5
            self.window.game.myMoneyInfo.allIn(self.window.game.cpuMoneyInfo)
            self.window.updateInfo()
            self.window.game.AIBetting = True
            for i in range(5):
                newImage = self.window.commonCards[i]
                self.window.commonCardImgs[i].config(image=newImage)
                self.window.commonCardImgs[i].image = newImage
            for i in range(2):
                newImage = self.window.cpuCards[i]
                self.window.cpuCardImgs[i].config(image=newImage)
                self.window.cpuCardImgs[i].image = newImage
            self.window.newGameBtn.config(text="결과 정산", command=self.window.game.endGame, bg="lime")
            self.window.makeButtonsGray()
        else:
            self.foldGame()


    
    # 현재 체크가 가능한지 확인 후 사용자에게 정말 체크할 것인지 재확인
    def confirmCheckGame(self):
        if (1 > self.window.game.turn or self.window.game.turn > 4):
            tkinter.messagebox.showwarning("알림", "게임 진행 중에만 체크가 가능합니다.")
            return
        checkGame = tkinter.messagebox.askokcancel("체크", "체크하시겠습니까?")
        if checkGame:
            self.checkGame()