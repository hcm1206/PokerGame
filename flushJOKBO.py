
def flush(deck): # 패(7장의 카드 정보 리스트)를 입력받아 이 패가 스트레이트이면 True, 아니면 False 반환
    deck.sort() # 먼저 입력받은 패를 정렬
    shapeList = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    for card in deck: # 패의 카드들을 불러와서 반복
        shapeList.append(card % 4) # 패의 7장의 카드들의 숫자 저장
        # 모듈러 연산을 해 나머지를 본다
    
    # 여기까지 하면 numList 리스트에는 패에 있는 7장의 카드들의 숫자들이 리스트로 저장되어 있음

    count2 = 0 # 카운트 변수 하나 생성하여 1로 설정
    curNum2 = shapeList[0] # 먼저 numList의 첫번째 원소(첫번째 카드 숫자)를 불러와 curNum에 저장
    
    #현재 첫번째 0번 인덱스인 d5(나머지연산으로 리스트에서는 1)

   # shapeList.count(1) # 1이 몇번나오는지 함수 하트의경우
   # shapeList.count(2) # 클라바
   # shapeList.count(3) # 다이아
   # shapeList.count(0) # 스페이드
    print(shapeList.count(1))
    print(shapeList.count(2))
    print(shapeList.count(3))
    print(shapeList.count(0))

    for i in range (4):
        if(shapeList.count(i)>=5):
            return True # 
    
    return False
        



deck=[5,9,13,17,21,16,15] # 문제의 7개 카드
deck2=[6,17,20,27,28,29,33]
print(flush(deck))
print(flush(deck2))