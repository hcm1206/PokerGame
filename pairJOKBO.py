def fourcard(deck): # 패(7장의 카드 정보 리스트)를 입력받아 이 패가 스트레이트이면 True, 아니면 False 반환
    deck.sort() # 먼저 입력받은 패를 정렬
    numList2 = [] # 패에 있는 7장의 카드들의 숫자를 저장할 빈 리스트 생성
    for card in deck: # 패의 카드들을 불러와서 반복
        numList2.append(card // 4) # 패의 7장의 카드들의 숫자 저장
        # 나누기 연산을 해 숫자만 봄
    
    # 여기까지 하면 numList 리스트에는 패에 있는 7장의 카드들의 숫자들이 리스트로 저장되어 있음

    curNum3 = numList2[0] # 현재에서는 1이 저장

    for i in range(1,len(numList2)): 
        if(numList2.count(i)==4): # 포카드
            print(numList2.count(i))
            print("이건 포카드")
            return True 
        elif(numList2.count(i)==3): # 트리플
            print(numList2.count(i))
            print("이건 트리플")
            return True
        elif(numList2.count(i)==2): # 원페어
            print(numList2.count(i))
            print("이건 원페어")
            return True
        
        elif(numList2.count(i)>=0): # 이건 노페어
            print(numList2.count(i))
            print("카드 족보싸움")
            return True
        
        '''
        elif(numList2.count(i)==2 and check):
            print(numList2.count(i))
            print("이건 투페어")
            return True
        '''



deck=[4,5,6,7,21,16,15] # 문제의 7개 카드
#4,5,10,11,21,16,15 투페어 조건 카드
#1,1,2,2,5,4,3
#s2 , h2 , c2 , d2 + h6,s5,d4
#4로 나눈다면 numlist에는 [1,1,1,1,5,4,3] 이렇게 옴 
deck2=[6,17,20,27,28,29,30]
#얘는 [1,4,5,6,7,7,7]
print(fourcard(deck))
print(fourcard(deck2))