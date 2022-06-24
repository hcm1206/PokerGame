from tkinter import *
from PIL import ImageTk, Image
import random
from Cards import Cards
from DisplayCard import DisplayCard

class Display:
    def __init__(self):
        window = Tk()
        window.title("Poker Game")

        cpuInfoFrame = Frame(window)
        cpuCardFrame = Frame(window)
        commonCardFrame = Frame(window)
        myCardFrame = Frame(window)
        buttonFrame = Frame(window)

        cpuInfoFrame.pack()
        cpuCardFrame.pack()
        commonCardFrame.pack()
        myCardFrame.pack()
        buttonFrame.pack()

        CardDeck = Cards()
        CardDeck.shuffleDeck()
        myCards = self.displayCardofDeck(CardDeck.drawMyCard())
        cpuCards = self.displayCardofDeck(CardDeck.drawCpuCard())
        commonCards = self.displayCardofDeck(CardDeck.drawInitCommonCard())
        backCard = self.displayBackCard()
        

        for i in range(3):
            Label(commonCardFrame, image=commonCards[i]).grid(row=0,column=i)
        
        for j in range(2):
            Label(commonCardFrame, image=backCard).grid(row=0,column=4+j)

        for i in range(2):
            Label(cpuCardFrame, image=cpuCards[i]).grid(row=0,column=i)
            Label(myCardFrame, image=myCards[i]).grid(row=0,column=i)


        window.mainloop()

    # 숫자 리스트를 입력하면 카드 이미지 객체 리스트로 변환
    def displayCardofDeck(self, deck):
        cards = []
        self.deck = deck
        for card in deck:
            cards.append(self.displayCard(card))
        return cards

    # 숫자를 입력하면 카드 이미지 객체로 변환
    def displayCard(self, num):
        self.height = 110
        self.width = 80
        self.n = num
        card = Image.open("card\d"+str(num)+".png")
        card = card.resize((self.width, self.height))
        card = ImageTk.PhotoImage(card)
        return card

    def displayBackCard(self):
        backCard = Image.open("card\d0.png")
        backCard = backCard.resize((self.width, self.height))
        backCard = ImageTk.PhotoImage(backCard)
        return backCard