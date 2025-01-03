from Card import Card
from Player import Player
from random import randrange
from card_methods import *

class Game():
    def __init__(self,players_names:list[str]):
        self.COLORS:list[str] = ["Red", "Green", "Blue", "Yellow"]
        self.deck:list[Card]=[]
        self.CARDS_PER_PLAYER:int = 6
        self.current_player:int = 0
        self.players:list[Player]=[]
        self.cards_on_table:list[Card]=[]
        self.direction:int=1
        self.number_of_players=len(players_names)
        self.create_deck()
        self.shuffle_deck()
        for i in players_names:
            self.players.append(Player(i,self))
        for player in self.players:
            for i in range(self.CARDS_PER_PLAYER):
                self.add_card_to_player(player)
        self.cards_on_table=[self.deck.pop()]
    def create_deck(self):
        for color in self.COLORS:
            for _ in range(2):
                self.deck.append(Card("reverse",color,reverse))
            for num in range(10):
                for _ in range(2):
                    self.deck.append(Card(num, color,do_nothing))
    def shuffle_deck(self):
        for i in range(len(self.deck)-1,0,-1):                      # Идем с конца массива
            j = randrange(i+1)                                      # Выбираем случайный индекс от 0 до i включительно
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i] # Меняем местами элементы
    def add_card_to_player(self,player:Player):
        if len(self.deck)==0:
            self.take_cards_from_table()
        player.add_card(self.deck.pop())
    def take_cards_from_table(self):
        self.deck+=self.cards_on_table[0:-1]
        self.cards_on_table=self.cards_on_table[-1:]
        self.shuffle_deck()
    def players_turn(self, player:Player,card:Card)->bool:
        if card.can_be_put_on_card(self.get_card_from_table()) and player==self.get_current_player():
            self.cards_on_table.append(card)
            card.function(self)
            self.set_next_player()
            return True
        return False
    def get_current_player(self):
        return self.players[self.current_player]
    def set_next_player(self):
        self.current_player=(self.current_player+self.direction+self.number_of_players) % self.number_of_players
    def get_card_from_table(self):
        return self.cards_on_table[-1]
    def run(self):
        game_finish=False
        while not game_finish:
            self.get_current_player().player_interface()
            for player in self.players:
                if len(player.hand)==0:
                    print(f"WIN: {player.name}")
                    game_finish=True