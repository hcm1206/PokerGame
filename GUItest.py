from tkinter import *
from PIL import ImageTk, Image
import random


class CardDeckTest:

    # 클래스 생성자
    def __init__(self):
        self.window = Tk() # self.window에 tkinter 화면 구성하겠다는 뜻
        self.height = 110 # 카드 이미지 높이
        self.width = 80 # 카드 이미지 폭
        self.window.title("Playing Cards") # window 창의 제목

        self.deck = [x for x in range(0,52)]

        

        cpuDeckFrame = Frame(self.window)
        cpuDeckFrame.pack()

        self.myDeckFrame = Frame(self.window)
        self.myDeckFrame.pack()

        buttonFrame = Frame(self.window)
        buttonFrame.pack()

        self.shuffleCard()

        Button(buttonFrame,text="Shuffle",command=self.shuffleCard).grid(row=1,column=0,columnspan=2)
        Button(buttonFrame,text="Sort",command=self.sortCard).grid(row=1,column=3,columnspan=2)

        self.window.mainloop()


    # 카드 덱을 무작위로 섞는 메소드
    def shuffleCard(self):
        random.shuffle(self.deck)
        self.displayCard(self.deck)

    # 카드를 카드번호 오름차순으로 정렬하는 메소드
    def sortCard(self):
        currentDeck = []
        for i in range(5):
            currentDeck.append(self.deck[i])
        currentDeck.sort()
        self.displayCard(currentDeck)

    # 카드를 화면에 출력하는 메소드
    def displayCard(self, deck):
        self.card = []
        for i in range(5):
            self.card.append(Image.open("card\d"+str(deck[i])+".png"))
            self.card[i] = self.card[i].resize((self.width, self.height))
            self.card[i] = ImageTk.PhotoImage(self.card[i])
            Label(self.myDeckFrame, image=self.card[i]).grid(row=0,column=i)




CardDeckTest()




