from Card import Card
from Player import Player
from random import randrange
from Restrictions import Restrictions
from card_methods import reverse,skip,add_2_cards,do_nothing,switch_color,add_4_cards

class Game():
    def __init__(self,players_names:list[str]):
        self.COLORS:list[str] = ["Red", "Green", "Blue", "Yellow"]
        self.BLACK="Black"
        self.deck:list[Card]=[]
        self.CARDS_PER_PLAYER:int = 6
        self.current_player:int = 0
        self.players:list[Player]=[]
        self.cards_on_table:list[Card]=[]
        self.direction:int=1
        self.number_of_players=len(players_names)
        self.create_deck()
        self.shuffle_deck()
        self.restrictions=Restrictions(self)
        for name in players_names:
            self.players.append(Player(name,self))
        for player in self.players:
            for i in range(self.CARDS_PER_PLAYER):
                self.add_card_to_player(player)
        for i in range(len(self.deck)):
            if self.deck[i].can_be_first:
                self.cards_on_table=[self.deck.pop(i)]
                break
        self.restrictions.update()
    def create_deck(self):
        for _ in range(4):
            self.deck.append(Card(self,"switch",self.BLACK,switch_color))
        for _ in range(4):
            self.deck.append(Card(self,"+4",self.BLACK,add_4_cards))
        for color in self.COLORS:
            for _ in range(2):
                self.deck.append(Card(self,"reverse",color,reverse))
            for _ in range(2):
                self.deck.append(Card(self,"skip",color,skip))
            for _ in range(2):
                self.deck.append(Card(self,"+2",color,add_2_cards))
            for num in range(10):
                for _ in range(2):
                    self.deck.append(Card(self,num, color,do_nothing,True))
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
        if card.can_be_put_on_table() and player==self.get_current_player():
            self.cards_on_table.append(card)
            self.restrictions.update()
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