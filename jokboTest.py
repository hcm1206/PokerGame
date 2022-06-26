import random
from tkinter import *
from PIL import ImageTk, Image

# 실행하면 GUI로 랜덤한 5개의 패가 생성되고 터미널에 카드 정보와 스트레이트 판정 결과(True or False)가 각각 뜨게 되어있음
# 이해하라고 친절하게 주석까지 달아놨으니 잘 보고 다른 족보 알고리즘들을 구현해오시오
# 테스트하기 좋게 GUI까지 적용해놨으니까 나중에 다른 족보 테스트할 때 써도 됨


# 스트레이트 체크하는 함수
def straight(deck): # 패(7장의 카드 정보 리스트)를 입력받아 이 패가 스트레이트이면 True, 아니면 False 반환
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    for card in deck: # 패의 카드들을 불러와서 반복
        numList.append(card // 4) # 패의 7장의 카드들의 숫자 저장
    
    # 여기까지 하면 numList 리스트에는 패에 있는 7장의 카드들의 숫자들이 리스트로 저장되어 있음

    count = 1 # 카운트 변수 하나 생성하여 1로 설정
    curNum = numList[0] # 먼저 numList의 첫번째 원소(첫번째 카드 숫자)를 불러와 curNum에 저장
    for i in range(1,len(numList)): # 1부터 6까지 반복
        if curNum + 1 == numList[i]: # 만약 현재 카드 숫자에서 1을 더한 값이 다음 카드 숫자와 같다면 (ex. 현재 카드 숫자(curNum)가 2인데 다음 카드 숫자(numList[i]가 3이면)
            count += 1 # 카운트를 1 올림
            curNum = numList[i] # 다음 카드 숫자를 현재 카드 숫자로 바꿈 (ex. 현재 카드 숫자(curNum)를 2에서 3으로 바꿈)
        elif curNum == numList[i]: # 현재 카드 숫자와 다음 카드 숫자가 같다면 (ex. 현재 카드 숫자(curNum)이 2인데 다음 카드 숫자(numList[i])도 2라면)
            pass # 아무것도 건들지 말고 그냥 통과
        else: # 다음 카드 숫자가 아예 다른 값이라면 (ex. 현재 카드 숫자(curNum)이 2인데 다음 카드 숫자(numList[i])가 5라면)
            count = 1 # 카운트 초기화
            curNum = numList[i] # 다음 카드 숫자를 현재 카드 숫자로 바꿈 (ex. 현재 카드 숫자(curNum)를 2에서 5로 바꿈)
        if count >= 5: # 카운트가 5가 넘었다면 (숫자들이 5개 연속으로 1씩 차이가 난다면)
            return True # 얘는 스트레이트다! ☆★☆ 빰빰빰 ☆★☆
    
    return False # 응 얘 스트레이트 아님 ㅅㄱ


# 이거는 그냥 GUI 용 ======
window = Tk()
window.title("Randomly Generated 5 Sets of 7 Cards")
height = 110
width = 80
# =========================





testDeck = [6,17,20,27,28,29,33] # 임의의 스트레이트를 만족하는 테스트용 패 (c2, h5, s6, d7, s8, h8, h9)

print(straight(testDeck)) # 테스트용 패가 스트레이트임? (당연히 True 출력)
print()

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
    Label(window, text="스트레이트☆★☆" if straight(select) else "스트레이트 아님").grid(row=i,column=7)
    # 여기까지 GUI용 ========================================================
    print(select) # 카드 번호 리스트 출력
    print(straight(select)) # 스트레이트인지 판정 (스트레이트면 True, 아니면 False)
    print()


window.mainloop() # GUI 실행

