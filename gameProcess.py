from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
from PIL import ImageTk, Image
from Cards import *
from money import *
from CheckJokbo import checkJokbo, getKicker
from gameSetting import Setting
from cpuTest import PrototypeAI

class GameProcess:
    # 상위 클래스 display를 받아옴
    def __init__(self, display):
        # 상위 window 클래스의 데이터나 메소드를 불러오고 싶다면 self.window.(데이터 or 메소드) 와 같이 불러와 사용 및 수정 가능
        self.display = display
        # self.에 Cards 객체 저장
        self.CardDeck = Cards()

        # 참여자들의 잔돈 상태를 저장할 클래스 선언
        self.cpuMoneyInfo = MoneyInfo()
        self.myMoneyInfo = MoneyInfo()

        # 현재 턴을 세는 변수
        self.turn = 0
        # 현재 턴에 배팅 과정이 진행되었는지 여부 판단하는 변수
        self.Betting = False

        # 현재 턴에서 배팅이 진행되어야(self.Betting = True를 만족해야) 다음 턴으로 진행할 수 있는 구조

        self.setting = Setting(self)

        self.AI = PrototypeAI(self)





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

        self.AI.initCard()


        for i in range(5):
            newImage = self.display.backCard
            self.display.commonCardImgs[i].config(image=newImage)
            self.display.commonCardImgs[i].image = newImage
        for i in range(2):
            newImage = self.display.backCard
            self.display.myCardImgs[i].config(image=newImage)
            self.display.myCardImgs[i].image = newImage
            self.display.cpuCardImgs[i].config(image=newImage)
            self.display.cpuCardImgs[i].image = newImage
        self.display.newGameBtn.config(text="게임 시작",command=self.startGame, bg="cyan", fg="black")
    

        

    
    # 게임 시작 (1턴)
    def startGame(self):
        self.turn = 1
        self.Betting = False
        self.cpuMoneyInfo.blind()
        self.myMoneyInfo.blind()
        self.display.updateInfo()

        for i in range(2):
            newImage = self.display.myCards[i]
            self.display.myCardImgs[i].config(image=newImage)
        
            self.AI.addCard(self.CardDeck.getCpuDeckCards()[i])

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
                newImage = self.display.commonCards[i]
                self.display.commonCardImgs[i].config(image=newImage)
                self.display.commonCardImgs[i].image = newImage

                self.AI.addCard(self.CardDeck.getCommonDeckCards()[i])

        # 현재 3턴 또는 4턴이면 공용카드 1장 공개
        else:
            newImage = self.display.commonCards[self.turn]
            self.display.commonCardImgs[self.turn].config(image=newImage)
            self.display.commonCardImgs[self.turn].image = newImage

            self.AI.addCard(self.CardDeck.getCommonDeckCards()[self.turn])

    # 게임 결과 보기 (5턴)
    def resultGame(self):
        self.turn = 5
        self.Betting = False
        self.display.newGameBtn.config(text="결과 정산", command=self.endGame, bg="lime")

        for i in range(2):
            newImage = self.display.cpuCards[i]
            self.display.cpuCardImgs[i].config(image=newImage)
            self.display.cpuCardImgs[i].image = newImage
        self.display.makeButtonsGray()

    # 게임 종료 및 족보 판정
    def endGame(self):
        myFinalCards = self.CardDeck.getMyDeckCards() + self.CardDeck.getCommonDeckCards()
        cpuFinalCards = self.CardDeck.getCpuDeckCards() + self.CardDeck.getCommonDeckCards()
        myJokbo, self.myScore = checkJokbo(myFinalCards)
        cpuJokbo, self.cpuScore = checkJokbo(cpuFinalCards)
        self.totalBetting = self.cpuMoneyInfo.getTotalBetting() + self.myMoneyInfo.getTotalBetting()
        myKicker = getKicker(self.CardDeck.getMyDeckCards(), self.myScore)
        cpuKicker = getKicker(self.CardDeck.getCpuDeckCards(), self.myScore)

        # 내 점수가 높으면 승리
        if self.myScore > self.cpuScore:
            self.winGame()
        
        # 상대 점수가 높으면 패배
        elif self.myScore < self.cpuScore:
            self.loseGame()
        
        # 점수가 동점이면 키커 비교
        else:

            # 내 키커가 더 높으면 승리
            if myKicker > cpuKicker:
                myJokbo += " | 키커 : " + str(self.changeCardNumber(myKicker))
                cpuJokbo += " | 키커 : " + str(self.changeCardNumber(cpuKicker))
                self.winGame()
            # 상대 키커가 더 높으면 패배
            elif myKicker < cpuKicker:
                myJokbo += " | 키커 : " + str(self.changeCardNumber(myKicker))
                cpuJokbo += " | 키커 : " + str(self.changeCardNumber(cpuKicker))
                self.loseGame()
            # 키커까지 똑같다면 무승부
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
    
    # 게임 승리
    def winGame(self):
        self.myMoneyInfo.addMoney(self.totalBetting)
        self.display.myMessage.configure(bg="lime")
        self.display.cpuMessage.configure(bg="orange")
    
    # 게임 패배
    def loseGame(self):
        self.cpuMoneyInfo.addMoney(self.totalBetting)
        self.display.myMessage.configure(bg="orange")
        self.display.cpuMessage.configure(bg="lime")

    # 무승부
    def drawGame(self):
        self.myMoneyInfo.addMoney(self.totalBetting//2)
        self.cpuMoneyInfo.addMoney(self.totalBetting//2)
        self.display.myMessage.configure(bg="orange")
        self.display.cpuMessage.configure(bg="orange")

    # 숫자 점수를 실제 포커 카드 숫자로 바꾸는 메소드
    def changeCardNumber(self, num):

        numList = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        return numList[num-1]
        
    # 결과 팝업 메시지 출력
    def showResult(self, myScore, cpuScore, myKicker, cpuKicker, totalBetting):
        if (myScore > cpuScore) or ((myScore == cpuScore) and (myKicker > cpuKicker)):
            tkinter.messagebox.showinfo("판돈 확보 성공", str(totalBetting) + "을 획득하였습니다.")
        elif (myScore < cpuScore) or ((myScore == cpuScore) and (myKicker < cpuKicker)):
            tkinter.messagebox.showinfo("핀돈 확보 실패", "상대방이 " + str(totalBetting) + "을 가져갑니다.")
        else:
            tkinter.messagebox.showinfo("무승부", "판돈의 절반 " + str(totalBetting//2) + "을 획득하였습니다.")

    # 게임 종료(누군가 돈을 다 잃었으면 게임 최종 종료, 아니면 현재 금액으로 새 게임 시작)
    def gameSet(self):
        if self.myMoneyInfo.getMoney() <= 0:
            tkinter.messagebox.showinfo("파산", "소지 금액을 모두 잃었으므로 게임에서 패배하였습니다.")
            self.display.newGameBtn.config(text="게임 초기화", command=self.setting.confirmInitMoney, bg="red", fg="white")
        elif self.cpuMoneyInfo.getMoney() <= 0:
            tkinter.messagebox.showinfo("승리", "상대방의 소지 금액이 모두 소진되어 게임에서 승리하였습니다.")
            self.display.newGameBtn.config(text="게임 초기화", command=self.setting.confirmInitMoney, bg="red", fg="white")
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