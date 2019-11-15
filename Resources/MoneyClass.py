class Money:
    def __init__(self, initial):
        self.total = initial
        self.sec = 1
        
    def moneySec(self):
        self.total += self.sec
        print(self.total)
    