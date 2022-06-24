def check1():
    
    def checkStraightFlush():
        cardnum[7] = {25,31,3,19,14,29,7}
        
    for i in range(len(cardnum)):
        # 카드 숫자 판정
        carddiv[i] = cardnum[i] // 4 #4로 나눈 몫 저장
        # 카드 무늬 판정
        cardmol = cardnum[i] % 4 #4로 나눈 나머지 저장

    # 카드 무늬 결정 장소
    if(cardmol==0):
        print("spade")
    if(cardmol==1):
        print("heart")
    if(cardmol==2):
        print("club")
    if(cardmol==3):
        print("diamond")
    
    print("숫자:"+str(carddiv[i]))
    



    #print("숫자"+str(carddiv))
    # 2022-05-22
