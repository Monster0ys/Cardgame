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
def switch_color(game:Game):
    pcolor=-1
    while pcolor<0 or pcolor>=len(game.COLORS):
        for i in range(len(game.COLORS)):
            print(f"[{i}] {game.COLORS[i]}")
        pcolor=int(input("Enter color: "))
    game.restrictions.allowed_colors=[game.COLORS[pcolor],'Black']
    game.restrictions.allowed_names=[]