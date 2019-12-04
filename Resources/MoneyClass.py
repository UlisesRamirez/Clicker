import sys
sys.path.insert(0, 'C:/Users/Ulises/Desktop/Projects/Python/Clicker')
from Resources.UpgradesClass import Upgrade

class Money:
    def __init__(self, initial):
        self.total = initial
        self.income = 1
        self.cost = 0
        self.upgradeCluster = {}
        while len(self.upgradeCluster) < 10:
            tempUpgrade = {}
            while len(tempUpgrade) < 10:
                basePrice = 1 + (100 * len(tempUpgrade)) * (len(self.upgradeCluster) + 1)
                income = 10 + (10 * len(tempUpgrade)) * (len(self.upgradeCluster) + 1)
                tempUpgrade[len(tempUpgrade) + 1] = Upgrade(basePrice, income, self)
            self.upgradeCluster[len(self.upgradeCluster) + 1] = tempUpgrade

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
        if upgrade in self.upgradeCluster:
            upgrade.buyUpgrade()
        else:
            print('Wrong name entered. ')
    
    def deupgrade(self, upgrade):
        if upgrade in self.upgradeCluster:
            upgrade.sellUpgrade()
        else:
            print('Wrong name entered. ')