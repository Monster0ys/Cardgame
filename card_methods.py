from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game

def reverse(game:Game):
    game.direction*=-1
def do_nothing(game:Game):
    pass