import random
from tkinter import *
from PIL import ImageTk, Image
from CheckJokbo import checkJokbo

# 족보(점수제) 테스트용 파일

# 이거는 그냥 GUI 용 ======
window = Tk()
window.title("Randomly Generated 5 Sets of 7 Cards")
height = 110
width = 80
# =========================


testDeck = [6,17,20,27,28,29,33] # 임의의 스트레이트를 만족하는 테스트용 패 (c2, h5, s6, d7, s8, h8, h9)
testDeck2 = [11,15,17,19,23,27,38] # 스트레이트플러시 예제 1
testDeck3 = [10,13,17,18,21,25,29] # 스트레이트플러시 예제 2
testDeck4 = [0,10,36,40,43,44,48] # 로얄스트레이트플러시 예제

#testDeck5 = [2,3,9,10,27,34,48] # A투페어 덱 A와 3 투페어인데 3투페어로 판정하는버그 / 22/07/05 / 성공 후 주석처리

#testDeck5 = [22,49,30,46,4,26,42] # Q플러시인데 하트A를 보고 최고 숫자로 보는듯

testDeck5 = [12,16,20,24,28,9,13]

debugDeck = [6,25,29,30,31,35,41] # 버그 수정용 덱
#debugDeck2 = [11,15,16,23,27,33,38]
#debugDeck3 = [4,22,26,30,42,46,49] # K 플러시 버그

print(checkJokbo(testDeck2))
print()
print(checkJokbo(testDeck3))
print()
print(checkJokbo(testDeck4)) # 로얄
print()
print(checkJokbo(testDeck5)) # 원래는 Q플러시로 판정
print("이게 플러시 오류 덱")
#print(checkJokbo(debugDeck3))
print()
'''
deck = [x for x in range(52)] # 카드 덱 생성
cardImgs = [] # 카드 이미지 객체 저장할 이차원 리스트 생성 (GUI용)

for i in range(5): # 랜덤으로 7장 선택한 5가지 패 (UI로 시각화)
    random.shuffle(deck) # 덱 셔플
    select = deck[0:7] # 셔플된 덱에서 7장 드로우하여 패 생성
    select.sort() # 생성한 패를 정렬
    # 이 아래는 GUI용 =======================================================
    cardImgs.append([])
    for j in range(len(select)):
        cardImgs[i].append(Image.open("card\d"+str(select[j])+".png"))
        cardImgs[i][j] = cardImgs[i][j].resize((width,height))
        cardImgs[i][j] = ImageTk.PhotoImage(cardImgs[i][j])
        Label(window, image=cardImgs[i][j]).grid(row=i,column=j)
    resultText = checkJokbo(select)
    Label(window, text=resultText[0] + "\nscore : " + str(resultText[1]), width=15).grid(row=i,column=7)
    # 여기까지 GUI용 ========================================================
    print(select) # 카드 번호 리스트 출력
    print()


window.mainloop() # GUI 실행
'''