from Resources import MoneyClass
from Resources import UpgradesClass

mainPlayer = MoneyClass.Money(100)
mainPlayer.initializeUpgrades()

# main game function, needs to read input and perform actions
# It's called in the final while loop
def inputClassification():
    function = input(': ').lower().split()
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
def Help(noun):
    print('This game is about gaining as much money as you can.')
    print('For that you have turns in wich you can pucharse upgrades,')
    print('upgrades cost a certain amount of money per turn')
    print('that you can check with the \'status\' command')
    inputClassification()

def Upgrade(noun):
    try:
        mainPlayer.upgrade(noun)
    except NameError:
        print('something went wrong. ')
    finally:
        inputClassification()

def Deupgrade(noun):
    try:
        mainPlayer.deupgrade(noun)
    except NameError:
        print('something went wrong. ')
    finally:
        inputClassification()

def checkStatus(noun):
    print('Your total money is {}'.format(mainPlayer.total))
    print('and your cost per turn is {}'.format(mainPlayer.cost))
    if mainPlayer.total - mainPlayer.cost < 0:
        print('You should sell some upgrades or you\'re going to lose soon')
    inputClassification()

def passTurn(noun):
    print('Starting next turn... ')
    checkStatus(noun)

def closing(noun):
    exit() 

# ---------- Setup of the functions dictionary ----------
# As the name says it's the dictionary of all the functions
functionDictionary = {
    'help': Help,
    'buy': Upgrade,
    'sell': Deupgrade,
    'status': checkStatus,
    'pass': passTurn,
    'exit': closing
}

# ------------------ Loop of the game ------------------
# goes to the main function, and loops until the game closes
# the other two functions manage the game money
while True:
    inputClassification()
    mainPlayer.moneySecond()
    mainPlayer.costsSecond()