from random import shuffle, randint
from copy import deepcopy
from time import sleep
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
    else: break

#run(loading(endDelay = 1000, start = True))

#---------Cards---------#
deck = [
    'g1',
    'g1',
    'g2',
    'g2',
    'g3',
    'g3',
    'g4',
    'g4',
    'g5',
    'g5',
    'g6',
    'g6',
    'g7',
    'g7',
    'g8',
    'g8',
    'g9',
    'g9',
    'g0',
    'g0',
    'gR',
    'gR',
    'gB',
    'gB',
    'g2+',
    'g2+',
    'b1',
    'b1',
    'b2',
    'b2',
    'b3',
    'b3',
    'b4',
    'b4',
    'b5',
    'b5',
    'b6',
    'b6',
    'b7',
    'b7',
    'b8',
    'b8',
    'b9',
    'b9',
    'b0',
    'b0',
    'bR',
    'bR',
    'bB',
    'bB',
    'b2+',
    'b2+',
    'y1',
    'y1',
    'y2',
    'y2',
    'y3',
    'y3',
    'y4',
    'y4',
    'y5',
    'y5',
    'y6',
    'y6',
    'y7',
    'y7',
    'y8',
    'y8',
    'y9',
    'y9',
    'y0',
    'y0',
    'yR',
    'yR',
    'yB',
    'yB',
    'y2+',
    'y2+',
    'r1',
    'r1',
    'r2',
    'r2',
    'r3',
    'r3',
    'r4',
    'r4',
    'r5',
    'r5',
    'r6',
    'r6',
    'r7',
    'r7',
    'r8',
    'r8',
    'r9',
    'r9',
    'r0',
    'r0',
    'rR',
    'rR',
    'rB',
    'rB',
    'r2+',
    'r2+',
    '4+',
    '4+',
    '4+',
    '4+',
    '4+',
    '4+',
    'wc',
    'wc',
    'wc',
    'wc',
    'wc',
    'wc'
]
nCards = [
    'g1',
    'g2',
    'g3',
    'g4',
    'g5',
    'g6',
    'g7',
    'g8',
    'g9',
    'g0',
    'b1',
    'b2',
    'b3',
    'b4',
    'b5',
    'b6',
    'b7',
    'b8',
    'b9',
    'b0',
    'y1',
    'y2',
    'y3',
    'y4',
    'y5',
    'y6',
    'y7',
    'y8',
    'y9',
    'y0',
    'r1',
    'r2',
    'r3',
    'r4',
    'r5',
    'r6',
    'r7',
    'r8',
    'r9',
    'r0',
]
sCards = [
    'gR',
    'gB',
    'g2+',
    'bR',
    'bB',
    'b2+',
    'yR',
    'yB',
    'y2+',
    'rR',
    'rB',
    'r2+',
]
bCards = [
    '4+',
    'wc',
]

#-Names of cards-#
Name = {
    'g1': 'Green 1',
    'g2': 'Green 2',
    'g3': 'Green 3',
    'g4': 'Green 4',
    'g5': 'Green 5',
    'g6': 'Green 6',
    'g7': 'Green 7',
    'g8': 'Green 8',
    'g8': 'Green 8',
    'g9': 'Green 9',
    'g0': 'Green 0',
    'gR': 'Green Reverse',
    'gB': 'Green Ban',
    'g2+': 'Green 2+',
    'b1': 'Blue 1',
    'b2': 'Blue 2',
    'b3': 'Blue 3',
    'b4': 'Blue 4',
    'b5': 'Blue 5',
    'b6': 'Blue 6',
    'b7': 'Blue 7',
    'b8': 'Blue 8',
    'b9': 'Blue 9',
    'b0': 'Blue 0',
    'bR': 'Blue Reverse',
    'bB': 'Blue Ban',
    'b2+': 'Blue 2+',
    'y1': 'Yellow 1',
    'y2': 'Yellow 2',
    'y3': 'Yellow 3',
    'y4': 'Yellow 4',
    'y5': 'Yellow 5',
    'y6': 'Yellow 6',
    'y7': 'Yellow 7',
    'y8': 'Yellow 8',
    'y9': 'Yellow 9',
    'y0': 'Yellow 0',
    'yR': 'Yellow Reverse',
    'yB': 'Yellow Ban',
    'y2+': 'Yellow 2+',
    'r1': 'Red 1',
    'r2': 'Red 2',
    'r3': 'Red 3',
    'r4': 'Red 4',
    'r5': 'Red 5',
    'r6': 'Red 6',
    'r7': 'Red 7',
    'r8': 'Red 8',
    'r9': 'Red 9',
    'r0': 'Red 0',
    'rR': 'Red Reverse',
    'rB': 'Red Ban',
    'r2+': 'Red 2+',
    'wc': 'Wild Card',
    '4+': '4+',
    'Green 1': 'g1',
    'Green 2': 'g2',
    'Green 3': 'g3',
    'Green 4': 'g4',
    'Green 5': 'g5',
    'Green 6': 'g6',
    'Green 7': 'g7',
    'Green 8': 'g8',
    'Green 9': 'g9',
    'Green 0': 'g0',
    'Green R': 'gR',
    'Green B': 'gB',
    'Green 2+': 'g2+',
    'Blue 1': 'b1',
    'Blue 2': 'b2',
    'Blue 3': 'b3',
    'Blue 4': 'b4',
    'Blue 5': 'b5',
    'Blue 6': 'b6',
    'Blue 7': 'b7',
    'Blue 8': 'b8',
    'Blue 9': 'b9',
    'Blue 0': 'b0',
    'Blue R': 'bR',
    'Blue B': 'bB',
    'Blue 2+': 'b2+',
    'Yellow 1': 'y1',
    'Yellow 2': 'y2',
    'Yellow 3': 'y3',
    'Yellow 4': 'y4',
    'Yellow 5': 'y5',
    'Yellow 6': 'y6',
    'Yellow 7': 'y7',
    'Yellow 8': 'y8',
    'Yellow 9': 'y9',
    'Yellow 0': 'y0',
    'Yellow R': 'yR',
    'Yellow B': 'yB',
    'Yellow 2+': 'y2+',
    'Red 1': 'r1',
    'Red 2': 'r2',
    'Red 3': 'r3',
    'Red 4': 'r4',
    'Red 5': 'r5',
    'Red 6': 'r6',
    'Red 7': 'r7',
    'Red 8': 'r8',
    'Red 9': 'r9',
    'Red 0': 'r0',
    'Red R': 'rR',
    'Red B': 'rB',
    'Red 2+': 'r2+',
    'Wild Card': 'wc'
    }
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
