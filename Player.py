from __future__ import annotations
from Card import Card
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game
class Player():
    def __init__(self,name:str,game:Game):
        self.name:str=name
        self.hand:list[Card]=[]
        self.game:Game=game
    def __str__(self):
        a=[]
        a.append(f'Player: {self.name}')
        for i in range(len(self.hand)):
            a.append(f'[{i}] {str(self.hand[i])}')
        return '\n'.join(a)
    def __repr__(self):
        return self.__str__()
    def add_card(self,card:Card):
        self.hand.append(card)
    def player_interface(self):
        print("\033[2J\033[H", end="")
        print(self)
        print(f'Card on table: {self.game.get_card_from_table()}')
        if self==self.game.get_current_player():
            pick=int(input("Enter card number: "))
            if pick >= 0 and pick < len(self.hand):
                if self.game.players_turn(self,self.hand[pick]):
                    self.hand.pop(pick)
            elif pick == -1:
                self.game.add_card_to_player(self)

        
        