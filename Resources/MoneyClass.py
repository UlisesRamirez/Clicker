class Money:
    def __init__(self, initial):
        self.total = initial
        self.sec = 1
        
    def moneySec(self):
        self.total += self.sec
        print(self.total)

    def upgrade(self):
        print('upgrade')

class Upgrade:
    def __init__(self):
        self.timesBought = 1
        self.price 