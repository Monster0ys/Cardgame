from random import randrange

colors = ["Red", "Green", "Blue", "Yellow"]


class Card():
    def __init__(self,num,color):
        self.number=num
        self.color=color
deck:list[Card]=[]
        
for color in colors:    
    for num in range(10):
        deck.append(Card(num, color))
        deck.append(Card(num, color))

def shuffle_deck(deck):
    for i in range(len(deck)-1,0,-1):   # Идем с конца массива
        j = randrange(i+1)              # Выбираем случайный индекс от 0 до i включительно
        deck[i], deck[j] = deck[j], deck[i] # Меняем местами элементы

shuffle_deck(deck)

def check_card_compatibility(card_on_table:Card, players_card:Card):
    if card_on_table.number == players_card.number or card_on_table.color == players_card.color:
        return True
    else:return False

num_players = 3
num_of_card = 6
cards_on_table=[deck.pop()]
players_hands=[]
for i in range(num_players):
    hand=[]
    for _ in range(num_of_card):
        hand.append(deck.pop())
    players_hands.append(hand)

def players_turn(num_player,num_card):
    if check_card_compatibility(cards_on_table[-1],players_hands[num_player][num_card]):
        cards_on_table.append(players_hands[num_player].pop(num_card))
        return True
    else:return False

def add_card_to_player(num_player):
    global deck
    global cards_on_table
    if len(deck) > 0:
        players_hands[num_player].append(deck.pop())
        return True
    elif len(cards_on_table)>1:
        deck=cards_on_table[0:-1]
        cards_on_table=cards_on_table[-1:]
        shuffle_deck(deck)
        players_hands[num_player].append(deck.pop())
        return True
    else:return False

for i in range(100):
    print(add_card_to_player(0))