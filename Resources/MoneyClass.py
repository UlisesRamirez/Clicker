class Money:
    def __init__(self, initial):
        self.total = initial
        self.income = 1
        
    def monetSecond(self):
        self.total += self.income
        print(self.total)

    def upgrade(self):
        print('upgrade')

class Upgrade:
    def __init__(self):
        self.timesBought = 1
        self.price = 10 * self.timesBought

    def buyUpgrade(self, buyer):
        buyer.income += 10 # Amount of increment for each turn
        self.timesBought += 1
        self.price = 10 * self.timesBought
        # Number of pucharses of the upgrade
        # defines the future price increasing exponentially
        
