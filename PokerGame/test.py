def Card1():
    
    #cardrank = ['1','2','3','4','5','6','7','8','9','10','11','12','13']

    

    cardnum = 23 

    # 카드 숫자 판정
    carddiv = cardnum // 4 #4로 나눈 몫 저장
    # 카드 무늬 판정
    cardmol = cardnum % 4 #4로 나눈 나머지 저장

    if(cardmol==0):
        print("spade")
    if(cardmol==1):
        print("heart")
    if(cardmol==2):
        print("club")
    if(cardmol==3):
        print("diamond")

    print("숫자"+str(carddiv))

Card1()