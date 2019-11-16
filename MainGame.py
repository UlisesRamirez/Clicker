from Resources import MoneyClass

# As the name says it's the dictionary of all the functions

functionDictionary = {
    'help': help
}
mainPlayer = MoneyClass.Money(100)

#main game loop, needs to read input and perform actions

def inputClassification(function):
    if function[0] in functionDictionary:
        verb = functionDictionary[function]
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
    print('')

def buy(noun):
    print('')
while True:
    command = str(input(': ').split())
    inputClassification(command)