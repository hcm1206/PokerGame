import random
from tkinter import *
from PIL import ImageTk, Image

# 테스트용 파일. 족보 판정 테스트용

# 실행하면 GUI로 랜덤한 5개의 패가 생성되고 터미널에 카드 정보와 스트레이트 판정 결과(True or False)가 각각 뜨게 되어있음
# 이해하라고 친절하게 주석까지 달아놨으니 잘 보고 다른 족보 알고리즘들을 구현해오시오
# 테스트하기 좋게 GUI까지 적용해놨으니까 나중에 다른 족보 테스트할 때 써도 됨

# 스트레이트플러시
def straightFlush(deck): # 패(7장의 카드 정보 리스트)를 입력받아 이 패가 스트레이트이면 True, 아니면 False 반환
    deck.sort() # 먼저 입력받은 패를 정렬
    curCard = deck[0]
    count = 1
    checkList = []
    score = -1
    straight = False
    for i in range(1,len(deck)): # 1부터 6까지 반복
        if (curCard + 4) // 4 == deck[i] // 4:
            count += 1 # 카운트를 1 올림
            if i == 1:
                checkList.append(curCard)
            checkList.append(deck[i])
            curCard = deck[i]
            num = (deck[i] // 4)
        elif curCard // 4 == deck[i] // 4:
            checkList.append(deck[i])
        else: 
            count = 1 # 카운트 초기화
            curCard = deck[i]
        if count >= 5:
            straight = True

    if straight:
        shapeList = []
        for card in checkList:
            shapeList.append(card%4)
        for i in range(4):
            if(shapeList.count(i)>=5):
                score = 900 + num + 2

    return score
        
        

        

# 포카드 체크
def fourCard(deck):
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    score = -1
    for card in deck: # 패의 카드들을 불러와서 반복
        numList.append(card // 4) # 패의 7장의 카드들의 숫자 저장
        # 나누기 연산을 해 숫자만 봄

    for i in range(13): 
        if(numList.count(i)==4): # 포카드
            score = 800 + i + 1
    return score

def fullHouse(deck):
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    triple = False
    pair = False
    score = -1
    for card in deck: # 패의 카드들을 불러와서 반복
        numList.append(card // 4) # 패의 7장의 카드들의 숫자 저장
        # 나누기 연산을 해 숫자만 봄

    for i in range(13): 
        if(numList.count(i)==3):
            triple = True
            num = i
        elif(numList.count(i)==2):
            pair = True
        if (triple and pair):
            score = 700 + num + 1
    return score


# 플러시 체크 (플러시는 아직 숫자 판정 없음, 무조건 A로 판정)
def flush(deck): # 패(7장의 카드 정보 리스트)를 입력받아 이 패가 스트레이트이면 True, 아니면 False 반환
    deck.sort() # 먼저 입력받은 패를 정렬
    shapeList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    score = -1
    for card in deck: # 패의 카드들을 불러와서 반복
        shapeList.append(card % 4) # 패의 7장의 카드들의 숫자 저장
        # 모듈러 연산을 해 나머지를 본다
    
    # 여기까지 하면 numList 리스트에는 패에 있는 7장의 카드들의 숫자들이 리스트로 저장되어 있음

    # shapeList.count(1) # 1이 몇번나오는지 함수 하트의경우
    # shapeList.count(2) # 클라바
    # shapeList.count(3) # 다이아
    # shapeList.count(0) # 스페이드

    for i in range (4):
        if(shapeList.count(i)>=5):
            score = 600 + 1
    
    return score

# 스트레이트 체크
def straight(deck): # 패(7장의 카드 정보 리스트)를 입력받아 이 패가 스트레이트이면 True, 아니면 False 반환
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    score = -1
    for card in deck: # 패의 카드들을 불러와서 반복
        numList.append(card // 4) # 패의 7장의 카드들의 숫자 저장
    
    # 여기까지 하면 numList 리스트에는 패에 있는 7장의 카드들의 숫자들이 리스트로 저장되어 있음

    count = 1 # 카운트 변수 하나 생성하여 1로 설정
    curNum = numList[0] # 먼저 numList의 첫번째 원소(첫번째 카드 숫자)를 불러와 curNum에 저장
    for i in range(1,len(numList)): # 1부터 6까지 반복
        if curNum + 1 == numList[i]: # 만약 현재 카드 숫자에서 1을 더한 값이 다음 카드 숫자와 같다면 (ex. 현재 카드 숫자(curNum)가 2인데 다음 카드 숫자(numList[i]가 3이면)
            count += 1 # 카운트를 1 올림
            curNum = numList[i] # 다음 카드 숫자를 현재 카드 숫자로 바꿈 (ex. 현재 카드 숫자(curNum)를 2에서 3으로 바꿈)
            num = curNum
        elif curNum == numList[i]: # 현재 카드 숫자와 다음 카드 숫자가 같다면 (ex. 현재 카드 숫자(curNum)이 2인데 다음 카드 숫자(numList[i])도 2라면)
            pass # 아무것도 건들지 말고 그냥 통과
        else: # 다음 카드 숫자가 아예 다른 값이라면 (ex. 현재 카드 숫자(curNum)이 2인데 다음 카드 숫자(numList[i])가 5라면)
            count = 1 # 카운트 초기화
            curNum = numList[i] # 다음 카드 숫자를 현재 카드 숫자로 바꿈 (ex. 현재 카드 숫자(curNum)를 2에서 5로 바꿈)
        if count >= 5: # 카운트가 5가 넘었다면 (숫자들이 5개 연속으로 1씩 차이가 난다면)
            score += 500 + num + 2
    
    return score



# 트리플 체크
def triple(deck): 
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    score = -1
    for card in deck: # 패의 카드들을 불러와서 반복
        numList.append(card // 4) # 패의 7장의 카드들의 숫자 저장
        # 나누기 연산을 해 숫자만 봄

    for i in range(13): 
        if(numList.count(i)==3): # 트리플
            score += 400 + i + 1
    return score

# 투페어 체크
def twoPair(deck):
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    count = 0
    score = -1
    num = 0
    for card in deck: # 패의 카드들을 불러와서 반복
        numList.append(card // 4) # 패의 7장의 카드들의 숫자 저장
        # 나누기 연산을 해 숫자만 봄

    for i in range(13): 
        if(numList.count(i)==2):
            if i > num:
                num = i
            count += 1
            if count >= 2:
                score = 300 + num + 1
    return score

def onePair(deck):
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    score = -1
    for card in deck: # 패의 카드들을 불러와서 반복
        numList.append(card // 4) # 패의 7장의 카드들의 숫자 저장
        # 나누기 연산을 해 숫자만 봄

    for i in range(13): 
        if(numList.count(i)==2):
            score = 200 + i + 1
    return score

def noPair(deck):
    deck.sort()
    return 100 + max(deck) // 4 + 1


def checkJokbo(deck):
    score = 0
    jokbo = ["노페어", "원페어", "투페어", "트리플", "스트레이트", "플러시", "풀하우스", "포카드", "스트레이트 플러시"]
    num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]

    if straightFlush(deck) != -1:
        score = straightFlush(deck)
    elif fourCard(deck) != -1:
        score = fourCard(deck)
    elif fullHouse(deck) != -1:
        score = fullHouse(deck)
    elif flush(deck) != -1:
        score = flush(deck)
    elif straight(deck) != -1:
        score = straight(deck)
    elif triple(deck) != -1:
        scpre = triple(deck)
    elif twoPair(deck) != -1:
        score = twoPair(deck)
    elif onePair(deck) != -1:
        score = onePair(deck)
    else:
        score = noPair(deck)
    print(score)
    strJokbo = jokbo[score // 100 - 1]
    strJokbo += " " + num[(score % 100)-1]
    numScore = score % 100
    if numScore == 1:
        score += 13
    return strJokbo, score

# 이거는 그냥 GUI 용 ======
window = Tk()
window.title("Randomly Generated 5 Sets of 7 Cards")
height = 110
width = 80
# =========================





testDeck = [6,17,20,27,28,29,33] # 임의의 스트레이트를 만족하는 테스트용 패 (c2, h5, s6, d7, s8, h8, h9)
testDeck2 = [11,15,17,19,23,27,38]
testDeck3 = [10,13,17,18,21,25,29]
debugDeck = [6,25,29,30,31,35,41]


print(straightFlush(debugDeck))
print(straightFlush(testDeck2))
print(straightFlush(testDeck3))

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
    # 족보 테스트 시 이 아래 부분만 바꾸면 됨 ++++++++++++++++++++++++++++++++++
    resultText = checkJokbo(select)
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Label(window, text=resultText[0] + "\nscore : " + str(resultText[1]), width=15).grid(row=i,column=7)
    # 여기까지 GUI용 ========================================================
    print(select) # 카드 번호 리스트 출력


window.mainloop() # GUI 실행
