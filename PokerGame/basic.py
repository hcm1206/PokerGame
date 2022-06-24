# deck에 0~51의 값 리스트로 저장
deck = [x for x in range(0,52)]

# suits에 스페이드, 하트, 다이아몬드, 클럽 리스트 저장
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

# ranks에 에이스, 2, 3, 4, 5, 6, 7, 8, 9, 10, 잭, 퀸, 킹 저장
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# random 라이브러리 불러오기
import random

# deck 리스트의 요소들의 순서를 섞어서 저장
random.shuffle(deck)

# 반복 변수 i를 이용하여 4번 반복
for i in range(4):
    # suit에 suits 리스트의 [deck 리스트의 [i]번째 인덱스의 요소에서 13을 나눈 몫]번째 인덱스의 요소 저장 (0~12는 스페이드, 13~25는 하트, 26~38은 다이아몬드, 39~51은 클럽으로 지정)
    suit = suits[deck[i]//13]
    # rank에 ranks 리스트의 [deck 리스트의 [i]번째 인덱스의 요소에서 13을 나눈 나머지]번째 인덱스의 요소 저장 (에이스~킹 지정)
    rank = ranks[deck[i]%13]
    # 해당 인덱스의 카드 정보 출력
    print("Card Number", deck[i], "is", rank, "of", suit)