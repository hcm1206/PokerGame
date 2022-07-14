# tkinter Label로 출력하는 이미지 config 작동 테스트 파일

from tkinter import *
from PIL import ImageTk, Image
import random

window = Tk()
window.title("Test")

imgFrame = Frame(window)
btnFrame = Frame(window)
imgFrame.pack()
btnFrame.pack()

width = 80
height = 110

def displayCard():
    num = random.randrange(52)
    card = Image.open("card\d"+str(num)+".png")
    card = card.resize((width, height))
    card = ImageTk.PhotoImage(card)
    return card

def displayBackCard():
    backCard = Image.open("card\dback.png")
    backCard = backCard.resize((width, height))
    backCard = ImageTk.PhotoImage(backCard)
    return backCard

def changeCard():
    for i in range(5):
        newImage = displayCard()
        cardImg[i].config(image=newImage)
        cardImg[i].image = newImage



backCard = displayBackCard()

cardImg = []
for i in range(5):
    cardImg.append(Label(imgFrame, image=backCard))
    cardImg[i].grid(row=0,column=i)

button = Button(btnFrame, text="카드 변경", command=changeCard)
button.pack()


window.mainloop()


# 이 테스트 파일에서는 이미지 변경이 잘만 되는데!
# 왜! 실제 포커 게임 파일에 적용하면 작동을 안 하는가!




