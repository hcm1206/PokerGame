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
testDeck10 = [46,42,38,34,50,31,27] # 로얄스트레이트 플러쉬(A스트레이트 플러쉬로 표현)

testDeck9 = [12,16,20,24,28,39,47] # 스트레이트 플러쉬

testDeck = [20,21,22,23,14,25,35] # 포카드

testDeck2 = [37,38,39,32,33,2,3] # 풀하우스

testDeck3 = [19,35,39,43,45,3,15] # 플러시

testDeck4 = [14,17,23,24,29,35,38] # 스트레이트

testDeck5 = [1,2,3,5,16,17,18] # 트리플

testDeck6 = [2, 6, 21, 31, 32, 40,41] # 원페어

testDeck7 = [46,38,31,20,13,11,1] # 노페어

testDeck8 = [34,35,48,49,10,13,24] # 투페어
'''
print(checkJokbo(testDeck10))
print("정상적으로는 로얄(A)스트레이트 플러쉬 / 점수 : 913") # 성공
print()
print(checkJokbo(testDeck9))
print("정상적으로는 9스트레이트 플러쉬 / 점수 : 908") # 성공
print()
print(checkJokbo(testDeck))
print("정상적으로는 7포카드 / 점수 : 806") # 성공
print()
print(checkJokbo(testDeck2))
print("정상적으로는 J풀하우스 / 점수 : 710") # 성공
print()
print(checkJokbo(testDeck3))
print("정상적으로는 Q플러쉬 / 점수 : 611") # 성공
print()
'''
print(checkJokbo(testDeck4))
print("정상적으로는 J스트레이트 / 점수 : 913") # 성공
print()
'''
print(checkJokbo(testDeck5))
print("정상적으로는 6트리플 / 점수:405") # 성공
print()
print(checkJokbo(testDeck8))
print("정상적으로는 A투페어 / 점수:313") # 성공
print()
print(checkJokbo(testDeck6))
print("정상적으로는 Q원페어 / 점수:211") # 성공
print()
print(checkJokbo(testDeck7))
print("정상적으로는 K노페어 / 점수:112") # 성공
print()
'''
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