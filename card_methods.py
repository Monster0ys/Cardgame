from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game import Game

number_of_cards_must_be_taken=0

def reverse(game:Game):
    game.direction*=-1

def do_nothing(game:Game):
    pass

def skip(game:Game):
    game.restrictions.allowed_names=["skip"]
    game.restrictions.allowed_colors=[]
    game.restrictions.allow_to_take_card=False
    def skip_penalty():
        game.set_next_player()
        game.restrictions.standard_update()
    game.restrictions.penalty=skip_penalty
    
def add_2_cards(game:Game):
    game.restrictions.allowed_names=["+2","+4"]
    game.restrictions.allowed_colors=[]
    game.restrictions.allow_to_take_card=False
    global number_of_cards_must_be_taken
    number_of_cards_must_be_taken+=2
    def add_2_cards_penalty():
        global number_of_cards_must_be_taken
        for _ in range(number_of_cards_must_be_taken):
            game.add_card_to_player(game.get_current_player())
        game.set_next_player()
        game.restrictions.standard_update()
        number_of_cards_must_be_taken=0
    game.restrictions.penalty=add_2_cards_penalty
    
def switch_color(game:Game):
    pcolor=-1
    while pcolor<0 or pcolor>=len(game.COLORS):
        for i in range(len(game.COLORS)):
            print(f"[{i}] {game.COLORS[i]}")
        pcolor=int(input("Enter color: "))
    game.restrictions.allowed_colors=[game.COLORS[pcolor],game.BLACK]
    game.restrictions.allowed_names=[]

def add_4_cards(game:Game):
    game.restrictions.allowed_names=["+2","+4"]
    game.restrictions.allowed_colors=[]
    game.restrictions.allow_to_take_card=False
    global number_of_cards_must_be_taken
    number_of_cards_must_be_taken+=4
    pcolor=-1
    while pcolor<0 or pcolor>=len(game.COLORS):
        for i in range(len(game.COLORS)):
            print(f"[{i}] {game.COLORS[i]}")
        pcolor=int(input("Enter color: "))
    def add_4_cards_penalty():
        global number_of_cards_must_be_taken
        for _ in range(number_of_cards_must_be_taken):
            game.add_card_to_player(game.get_current_player())
        game.set_next_player()
        game.restrictions.allowed_colors=[game.COLORS[pcolor],game.BLACK]
        game.restrictions.allowed_names=[]
        number_of_cards_must_be_taken=0
        game.restrictions.allow_to_take_card=True
    game.restrictions.penalty=add_4_cards_penalty
    
