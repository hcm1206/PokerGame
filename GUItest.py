from tkinter import *
from PIL import ImageTk, Image
import random


class CardDeckTest:


    def __init__(self):
        self.window = Tk()
        self.height = 110
        self.width = 80


        self.deck = [x for x in range(0,52)]

        self.shuffleCard()

        Button(self.window,text="Shuffle",command=self.shuffleCard).grid(row=1,column=0,columnspan=5)

        self.window.mainloop()


    def shuffleCard(self):
        self.card = []
        random.shuffle(self.deck)
        for i in range(5):
            self.card.append(Image.open("card\c"+str(self.deck[i])+".png"))
            self.card[i] = self.card[i].resize((self.width, self.height))
            self.card[i] = ImageTk.PhotoImage(self.card[i])
            Label(self.window, image=self.card[i]).grid(row=0,column=i)
    
    def sortCard(self):
        pass
        # self.card


CardDeckTest()




