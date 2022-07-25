from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

class Setting:
    def __init__(self, game):
        self.game = game

    def initMoney(self):
        self.game.myMoneyInfo.initMoney()
        self.game.cpuMoneyInfo.initMoney()
        self.game.initGame()
    
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
        self.game.cpuMoneyInfo.setBlind(newBlind)
        self.game.myMoneyInfo.setBlind(newBlind)
        self.game.display.updateInfo()
        if self.game.turn != 0:
            tkinter.messagebox.showinfo("알림", "다음 게임부터 " + str(newBlind) + "의 블라인드가 적용됩니다.")