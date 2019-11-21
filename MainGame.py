from Resources import MoneyClass

# As the name says it's the dictionary of all the functions

mainPlayer = MoneyClass.Money(100)

#main game loop, needs to read input and perform actions

def inputClassification(function):
    print(function[0])
    if function[0] in functionDictionary:
        verb = functionDictionary[function[0]]
    else:
        print("Unknown function {}".format(function))
        print("Type help for a list of the commands. ")
        return
    
    if len(function) >= 2:
        argument = function[1]
        print(verb(argument))
    else:
        print(verb("nothing"))

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
        return('Next move. ')

def checkStatus(noun):
    print('unfinished')

functionDictionary = {
    'help': help,
    'buy': Upgrade,
    'status': checkStatus
}

while True:
    command = input(': ').split()
    inputClassification(command)