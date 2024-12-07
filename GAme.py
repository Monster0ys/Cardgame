from random import randrange

colors = ["Red", "Green", "Blue", "Yellow"]


class Card():
    def __init__(self,num,color):
        self.number=num
        self.color=color
arr:list[Card]=[]
        
for color in colors:    
    for num in range(10):
        arr.append(Card(num, color))
        arr.append(Card(num, color))

def shuffle_array(arr):
    for i in range(len(arr) -1,0,-1):   # Идем с конца массива
        j = randrange(i+1)              # Выбираем случайный индекс от 0 до i включительно
        arr[i], arr[j] = arr[j], arr[i] # Меняем местами элементы

shuffle_array(arr)

def check_card_compatibility(card_on_table:Card, players_card:Card):
    if card_on_table.number == players_card.number or card_on_table.color == players_card.color:
        return True
    else:return False

num_players = 3
num_of_card = 6
cards_on_table=[arr.pop()]
players_hands=[]
for i in range(num_players):
    hand=[]
    for _ in range(num_of_card):
        hand.append(arr.pop())
    players_hands.append(hand)

print(cards_on_table[0].number,cards_on_table[0].color,players_hands[0][0].number, players_hands[0][0].color)
print(check_card_compatibility(cards_on_table[0],players_hands[0][0]))
   
