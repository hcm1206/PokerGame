from PIL import ImageTk, Image

class DisplayCard():
    def __init__(self, num):
        self.height = 110
        self.width = 80
        self.n = num
        self.card = Image.open("card\d"+str(num)+".png")
        self.card = self.card.resize((self.width, self.height))
        self.card = ImageTk.PhotoImage(self.card)
        


