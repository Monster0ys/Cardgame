from Card import Card

class Player():
    hand:list[Card]=[]
    def __init__(self):
        self.hand=[]
    def __str__(self):
        a=[]
        for i in range(len(self.hand)):
            a.append(f'[{i}] {str(self.hand[i])}')
        return '\n'.join(a)
    def __repr__(self):
        return self.__str__()
    def add_card(self,card:Card):
        self.hand.append(card)
