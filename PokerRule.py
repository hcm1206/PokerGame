class PokerRule:
    def __init__(self):
    
        self.seven_list=[42,34,30,26,22,18,4] # 테스트 할 7개 원소의 카드 숫자 값
        
        

        self.panjung() # 문양 판정이

    def sevenCards(self,seven_list): # 7개의 숫자가 있는 리스트가 입력으로 들어올거임
        self.checklist = self.seven_list  # checklist를 갖고 판정할거라서 여기에 대입
    
    def numcheck(self): # 숫자 체크
        
        for i in range(len(checklist)): # 7개 원소가 있는 리스트 크기만큼 반복

            # 카드 무늬 판정
            #self.shapelist[i] = self.checklist[i] // 4  #4로 나눈 몫 저장
            self.cardshape[i] = self.checklist[i] % 4 #4로 나눈 나머지 저장

            # 카드 숫자 판정
            

# 클래스 전체 내부에서 쓸 변수는 self
# 클래스 내부 그리고 메소드 내부에서 쓸꺼면 안붙임 일단 다붙이고 보셈

    def panjung(self):
    # 카드 무늬 결정 장소
        for i in range(len(checklist)):
            
            if(self.cardshape==0):
                print("spade") # 나머지 0 스페이드
            if(self.cardshape==1):
                print("heart")
            if(self.cardshape==2):
                print("club")
            if(self.cardshape==3):
                print("diamond")
    
        print("문양인데요삐약삐약"+str(self.cardshape[i]))
    

PokerRule()

#--------------------------------------여기까지 문양만 판정하는 내용-------------------------------------------------------

#--------------------------------------아 부분부터 포커 족보 판정할거임------------------------------------

# 딕셔너리 자료형
# 플러쉬 판정 
# key값 그리거 value값에서 value

    #조건 : 문양이 모두 같으면서 숫자가 순서대로 정렬되어 있는 상태
   # def ChcekStraightFlush(checklist):
    #    checklist.sort() # 정렬 끝
