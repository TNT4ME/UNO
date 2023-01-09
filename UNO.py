from random import shuffle, randint
from copy import deepcopy
from time import sleep
from json import load
from asyncio import run
from os import system

def s(ms = 1000):
    '''Delay in milliseconds'''
    ms /= 1000
    sleep(ms)
def cls():
        system('cls')
async def loading(message = 'Loading', iterations = 3, speed = 250, endDelay = 500, start = False):

    _iter = iterations
    msg = message

    cls()

    if start:
        for i in range(1, _iter + 1):
            print('UNO\n' + msg + '.')
            s(speed)
            cls()
            print('UNO\n' + msg + '..')
            s(speed)
            cls()
            print('UNO\n' + msg + '...')
            s(speed)
            cls()
            print('UNO\n' + msg + '')
            if i == _iter:
                s(endDelay)
                cls()
            else:
                s(speed)
                cls()
    else:
        for i in range(1, _iter + 1):
            print(msg + '.')
            s(speed)
            cls()
            print(msg + '..')
            s(speed)
            cls()
            print(msg + '...')
            s(speed)
            cls()
            print(msg + '')
            if i == _iter:
                s(endDelay)
                cls()
            else:
                s(speed)
                cls()

#cls()
#s()
#print('UNO')
#s(1500)

Player = {
    # Human
    0: {
    'name': None,
    'banned': False,
    'victory': False,
    'cards': []
    },
    
    # Bots
    1: {
    'name': 'Bot1',
    'banned': False,
    'victory': False,
    'cards': []
    },
    2: {
    'name': 'Bot2',
    'banned': False,
    'victory': False,
    'cards': []
    },
    3: {
    'name': 'Bot3',
    'banned': False,
    'victory': False,
    'cards': []
    },
    4: {
    'name': 'Bot4',
    'banned': False,
    'victory': False,
    'cards': []
    },
    5: {
    'name': 'Bot5',
    'banned': False,
    'victory': False,
    'cards': []
    }
}

# Player name
while True:
    name = Player[0]['name'] = 'lol'#input('Player 1: ')

    if len(name) > 10:
        print('Name cannot more than 10 characters')
    elif not name.isalnum:
        print('Name cannot contain special characters')
    else:break

#run(loading(endDelay = 1000, start = True))

#---------Cards---------#
deck = load(open('cards/deck.json'))
nCards = load(open('cards/nCards.json'))
sCards = load(open('cards/sCards.json'))
bCards = load(open('cards/bCards.json'))

#-Names of cards-#
Name = load(open('cards/Names.json'))
#----------------#

randDeck = deepcopy(deck)
shuffle(randDeck)
#-----------------------#

# Starting card
while True:
    startCard = randDeck[len(randDeck) - 1]
    if startCard in nCards:
        break
    shuffle(randDeck)

# Giving cards to players
for p in range(6):
    for c in range(7):
        Player[p]['cards'].append(randDeck[0])
        randDeck.pop(0)

# Gameplay
gameHistory = []

print(Name[startCard])
s(500)

while True:
    # Human
    if not Player[0]['banned']:
        # Shows ur cards
        print('\nYour cards-')
        for c in range(len(Player[0]['cards'])):
            print(Name[Player[0]['cards'][c]])

        # Input
        card0 = input(f'\n{name}: ')

        # Makes sure u have the card played
        while True:
            try:
                if Name[card0] in Player[0]['cards']:
                    break
                elif Name[card0] in deck:
                    print("You don't have this card")
                    card0 = input(f'\n{name}: ')
            except:
                print('This is not a card')
                card0 = input(f'\n{name}: ')
        
        gameHistory.append(Name[card0])

    # todo
    # Bots
    if not Player[1]['banned']:
        pass
    break

quit()
