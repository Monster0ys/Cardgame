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
        self.allow_to_take_card:bool=True
    def update(self,allowed_colors=None,allowed_names=None, penalty=None, allow_to_take_card=None):
        self.allowed_colors=allowed_colors if allowed_colors is not None else [self.game.get_card_from_table().color,self.game.BLACK]
        self.allowed_names=allowed_names if allowed_names is not None else [self.game.get_card_from_table().name]
        self.penalty=penalty if penalty is not None else self.nothing
        self.allow_to_take_card=allow_to_take_card if allow_to_take_card is not None else True
    def nothing(self):
        pass