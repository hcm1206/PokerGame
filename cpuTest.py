from CheckJokbo import checkJokbo

class PrototypeAI:
    def __init__(self):
        self.nowDeck = []
        self.decision = 0
        
    def initCard(self):
        self.nowDeck = []
    
    def decision(self, newCard, playerBetting):
        self.nowDeck.append(newCard)
        jokbo, score = checkJokbo(self.nowDeck)
        return self.decision