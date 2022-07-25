from CheckJokbo import checkJokbo

class PrototypeAI:
    def __init__(self):
        self.nowDeck = []
        
    def initCard(self):
        self.nowDeck = []
    
    def decision(self, newCard, playerBetting):
        self.nowDeck.append(newCard)
        jokbo, score = checkJokbo(self.nowDeck)
        if playerBetting == 0:
            return 0
        else:
            if score >= 100:
                return playerBetting
            else:
                return -1