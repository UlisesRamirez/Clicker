from Resources.UpgradesClass import Upgrade

class Money:
    def __init__(self, initial):
        self.total = initial
        self.income = 1
        self.cost = 0
    
    def initializeUpgrades(self):
        upgradesCount = 0
        upgrades = []
        upgradesReferences = []

        while upgradesCount < 10:
            basePrice = 1 + (100 * len(upgrades))
            income = 10 + (10 * len(upgrades))
            upgrades.append(Upgrade(basePrice, income, self))
            for upgrade in upgrades:
                upgradesReferences.append('0')
            upgradesCount += 1

    def moneySecond(self):
        self.total += self.income

    def costsSecond(self):
        self.total -= self.cost
        if self.total - self.cost < 0:
            print('You lose')
            exit()
        elif self.total - (self.cost * 2) < 0:
            print('You\'re going to lose in the next turn...')
            print('Do something about it')

    def upgrade(self, upgrade):
        upgrade.buyUpgrade()
    
    def deupgrade(self, upgrade):
        upgrade.sellUpgrade()