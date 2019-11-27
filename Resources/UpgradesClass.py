class Upgrade:
    def __init__(self, basePrice, income, owner):
        self.cost = 1
        self.timesBought = 1
        self.added = income
        self.price = basePrice
        self.propietary = owner

    def buyUpgrade(self):
        if self.propietary.total - self.price >= 0:
            self.propietary.income += self.added # Amount of increment for each turn
            self.propietary.cost += self.cost
            self.propietary.total -= self.price
            self.timesBought += 1
            self.price = 10 * self.timesBought
            self.cost = 1 * self.timesBought
        else:
            print('Not enough money')
        # Number of pucharses of the upgrade
        # defines the future price increasing exponentially
    
    def sellUpgrade(self):
        if self.timesBought > 1:
            print('do you want to sell this upgrade?')
            check = input('Answer with yes or no... ').lower()
            if check == 'yes':
                self.propietary.income -= self.added
                self.propietary.income -= self.cost
                self.propietary.total += self.price
                self.timesBought -= 1
                self.price = 10 * self.timesBought
                self.cost = 1 * self.timesBought
            else:
                print('You answered no...')
        else:
            print('You don\'t have enough upgrades to sell. ')