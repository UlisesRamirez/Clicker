class Upgrade:
    def __init__(self, basePrice, income):
        self.timesBought = 1
        self.price = basePrice
        self.added = income
        self.cost = 1


    def buyUpgrade(self, buyer):
        if buyer.total - self.price >= 0:
            buyer.income += self.added # Amount of increment for each turn
            buyer.cost += self.cost
            buyer.total -= self.price
            self.timesBought += 1
            self.price = 10 * self.timesBought
            self.cost = 1 * self.timesBought
        else:
            print('Not enough money')
        # Number of pucharses of the upgrade
        # defines the future price increasing exponentially