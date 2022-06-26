import random
from tkinter import *
from PIL import ImageTk, Image

def straight(deck): # 패를 입력하여 이 패가 스트레이트이면 True, 아니면 False 반환
    deck.sort()
    numList = []
    for card in deck:
        numList.append(card // 4)
    count = 1
    curNum = numList[0]
    for i in range(1,len(numList)):
        if curNum + 1 == numList[i]:
            count += 1
            curNum = numList[i]
        elif curNum == numList[i]:
            pass
        else:
            curNum = numList[i]
            count = 1
        if count >= 5:
            return True
    
    return False

window = Tk()
window.title("Randomly Generated 5 Sets of 7 Cards")
height = 110
width = 80






testDeck = [6,17,20,27,28,29,33] # 임의의 스트레이트를 만족하는 패 (c2, h5, s6, d7, s8, h8, h9)

print(straight(testDeck))
print()

deck = [x for x in range(52)]
cardImgs = []

for i in range(5): # 랜덤으로 7장 선택한 5가지 패 (UI로 시각화)
    random.shuffle(deck)
    select = deck[0:7]
    select.sort()
    cardImgs.append([])
    for j in range(len(select)):
        cardImgs[i].append(Image.open("card\d"+str(select[j])+".png"))
        cardImgs[i][j] = cardImgs[i][j].resize((width,height))
        cardImgs[i][j] = ImageTk.PhotoImage(cardImgs[i][j])
        Label(window, image=cardImgs[i][j]).grid(row=i,column=j)
    print(select)
    print(straight(select))
    print()


window.mainloop()

