from __future__ import annotations
from card_methods import do_nothing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game
colors = {
    "Red":"\033[38;5;1m",
    "Green":"\033[38;5;10m",
    "Blue":"\033[38;5;21m",
    "Yellow":"\033[38;5;227m",
    "END":"\033[39m"
}

class Card():
    def __init__(self,game:Game=None,name:str="name",color:str="color",function:callable=do_nothing,can_be_first:bool=False):
        self.name:str=name
        self.color:str=color
        self.function:callable=function
        self.game:Game=game
        self.can_be_first:bool=can_be_first
    def __str__(self):
        return f"{str(self.name)} {colors[self.color] if self.color in colors else ''}{self.color}{colors['END']}"
    def __repr__(self):
        return self.__str__()
    def can_be_put_on_table(self):
        return self.name in self.game.restrictions.allowed_names or self.color in self.game.restrictions.allowed_colors
