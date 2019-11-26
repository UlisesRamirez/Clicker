from Resources import MoneyClass
from Resources import UpgradesClass

mainPlayer = MoneyClass.Money(100)

# --------------- Upgrades initialization ---------------
upgradesCount = 0
upgrades = []

while upgradesCount < 10:
    upgrades.append(UpgradesClass.Upgrade(1 + (100 * len(upgrades)), 10 + (10 * len(upgrades))))
    upgradesCount += 1

# main game loop, needs to read input and perform actions
def inputClassification():
    function = input(': ').split()
    if function[0] in functionDictionary:
        verb = functionDictionary[function[0]]
    else:
        print("Unknown function {}".format(function))
        print("Type help for a list of the commands. ")
        return
    
    if len(function) >= 2:
        argument = function[1]
        verb(argument)
    else:
        verb("nothing")

# -------------- Game functions definitions -------------
def help(noun):
    print('This game is about gaining as much money as you can.')
    print('For that you have turns in wich you can pucharse upgrades,')
    print('upgrades cost a certain amount of money per turn')
    print('that you can check with the \'status\' command')

def Upgrade(noun):
    try:
        noun.buyUpgrade(mainPlayer)
    except NameError:
        print('no upgrade {} is available'.format(noun))
    finally:
        inputClassification()

def checkStatus(noun):
    print('unfinished')

def closing(noun):
    exit() 

# ---------- Setup of the functions dictionary ----------
# As the name says it's the dictionary of all the functions
functionDictionary = {
    'help': help,
    'buy': Upgrade,
    'status': checkStatus,
    'exit': closing
}

while True:
    inputClassification()
    mainPlayer.moneySecond()
    mainPlayer.costsSecond()
    count = 0
    for upgrade in upgrades:
        print(upgrades[count].price)
        count += 1