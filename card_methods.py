from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game

def reverse(game:Game):
    game.direction*=-1
def do_nothing(game:Game):
    pass
def skip(game:Game):
    game.set_next_player()
def add_2_cards(game:Game):
    game.set_next_player()
    for _ in range(2):
        game.add_card_to_player(game.get_current_player())