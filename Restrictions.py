from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game


class Restrictions():
    def __init__(self,game:Game):
        self.allowed_colors:list[str]=[]
        self.allowed_names:list[str]=[]
        self.penalty:callable=self.nothing
        self.game:Game=game
    def standard_update(self):
        self.allowed_colors=[self.game.get_card_from_table().color,self.game.BLACK]
        self.allowed_names=[self.game.get_card_from_table().name]
        self.penalty=self.nothing
    def nothing(self):
        pass