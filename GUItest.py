from tkinter import *
from PIL import ImageTk, Image
import random


class CardDeckTest:


    def __init__(self):
        self.window = Tk()
        self.height = 110
        self.width = 80
        self.window.title("Playing Cards")


        self.deck = [x for x in range(0,52)]

        self.shuffleCard()

        Button(self.window,text="Shuffle",command=self.shuffleCard).grid(row=1,column=0,columnspan=2)
        Button(self.window,text="Sort",command=self.sortCard).grid(row=1,column=3,columnspan=2)

        self.window.mainloop()


    def shuffleCard(self):
        random.shuffle(self.deck)
        self.displayCard(self.deck)

    
    def sortCard(self):
        currentDeck = []
        for i in range(5):
            currentDeck.append(self.deck[i])
        currentDeck.sort()
        self.displayCard(currentDeck)


    def displayCard(self, deck):
        self.card = []
        for i in range(5):
            self.card.append(Image.open("card\d"+str(deck[i])+".png"))
            self.card[i] = self.card[i].resize((self.width, self.height))
            self.card[i] = ImageTk.PhotoImage(self.card[i])
            Label(self.window, image=self.card[i]).grid(row=0,column=i)


CardDeckTest()




