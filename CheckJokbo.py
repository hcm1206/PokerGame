# 족보 판정용 모듈 파일
# 다른 파일에서 족보판정을 할 때 from CheckJokbo import checkjokbo를 먼저 입력한 후 checkjokbo() 함수를 사용하면 됨


def straightFlush(deck):
    deck.sort() # 먼저 입력받은 패를 정렬
    curCard = deck[0]
    count = 1
    checkList = []
    checkRoyalList = []
    checkRoyalNumList = []
    score = -1
    straight = False

    for i in range(len(deck)): # 6까지 반복
        if (curCard + 4) // 4 == deck[i] // 4: # deck[12,16,20,24,28,9,13] = 8 스트레이트 플러쉬 28이 스페이드 8
            count += 1 # 카운트를 1 올림
            if i == 0:
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

    
    
    for card in deck:
        if (card // 4) in [13,9,10,11,12]:
            checkRoyalList.append(card)
            checkRoyalNumList.append(card // 4)



    if straight:
        score = 900 + num + 1
    if set([13,9,10,11,12]) <= set(checkRoyalNumList):
        checkList = checkRoyalList
        score = 901
        return score

    

    if score != -1:
        shapeList = []
        for card in checkList:
            shapeList.append(card % 4) # 0,1,2,3 문양을 보겠다
        for i in range(4):
            if(shapeList.count(i)>=5):
                return score
        score = -1

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
    numList = []
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
            shape = i # shape에 i가 0이면 스페이드 , 1이면 하트 , 2면 클로버 , 3이면 다이아몬드
            score = 600 # 플러쉬 점수를 600점 지급
    
    if score == 600: # 플러쉬 점수라면?
        for card in deck: # 0부터 6까지 7번 반복
            if card % 4 == shape: 
                numList.append(card // 4)
        score += max(numList)+1
        if 0 in numList:
            score = 601
    return score



# 스트레이트 체크 (셋(set) 자료구조를 사용한 새로운 로직)
def straight(deck): # 패(7장의 카드 정보 리스트)를 입력받아 이 패가 스트레이트이면 True, 아니면 False 반환
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    score = -1
    for card in deck:
        numList.append(card // 4)
    for i in range(9):
        checkDeck = []
        if set([0,9,10,11,12]) <= set(numList):
            score = 501
            break
        for j in range(i, i+5):
            checkDeck.append(j)
        if set(checkDeck) <= set(numList):
            score = 500 + i + 5
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
            if i == 0:
                score = 401
            else:
                score = 400 + i + 1
    return score

# 투페어 체크
def twoPair(deck):
    deck.sort() # 먼저 입력받은 패를 정렬
    numList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    count = 0
    score = -1
    num = -1
    for card in deck: # 패의 카드들을 불러와서 반복
        numList.append(card // 4) # 패의 7장의 카드들의 숫자 저장
        # 나누기 연산을 해 숫자만 봄

    for i in range(14): 
        if(numList.count(i)==2):
            if num != 0 and i > num:
                num = i
            elif i == 0:
                num = 0
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
            if i == 0:
                score = 201
            else:
                score = 200 + i + 1
    return score

def noPair(deck):
    deck.sort()
    numList = []
    for card in deck:
        numList.append(card//4)
    if 0 in numList:
        return 101
    else:
        return 100 + max(numList) + 1


def checkJokbo(deck):
    jokbo = ["노페어", "원페어", "투페어", "트리플", "스트레이트", "플러시", "풀하우스", "포카드", "스트레이트 플러시"]
    num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    score = getScore(deck)

    
    strJokbo = num[(score % 100)-1]
    strJokbo += " " + jokbo[score // 100 - 1]
    numScore = score % 100
    if numScore == 1:
        score += 13
    return strJokbo, score

def getScore(deck):
    score = straightFlush(deck)
    if score != -1:
        return score
    score = fourCard(deck)
    if score != -1:
        return score
    score = fullHouse(deck)
    if score != -1:
        return score
    score = flush(deck)
    if score != -1:
        return score
    score = straight(deck)
    if score != -1:
        return score
    score = triple(deck)
    if score != -1:
        return score
    score = twoPair(deck)
    if score != -1:
        return score
    score = onePair(deck)
    if score != -1:
        return score
    score = noPair(deck)
    return score