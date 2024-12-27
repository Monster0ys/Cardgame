from Card import Card
from Player import Player
from random import randrange

class Game():
    COLORS:list[str] = ["Red", "Green", "Blue", "Yellow"]
    deck:list[Card]=[]
    CARDS_PER_PLAYER:int = 6
    current_player:int = 0
    players:list[Player]=[]
    number_of_players:int=0
    cards_on_table:list[Card]=[]
    def __init__(self,players_names:list[str]):
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
            for num in range(10):
                self.deck.append(Card(num, color))
                self.deck.append(Card(num, color))
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
    def players_turn(self, player:Player,number_of_card:int):
        if player.hand[number_of_card].can_be_put_on_card(self.get_card_from_table()) and player==self.get_current_player():
            self.cards_on_table.append(player.hand.pop(number_of_card))
            self.set_next_player()
    def get_current_player(self):
        return self.players[self.current_player]
    def set_next_player(self):
        self.current_player=(self.current_player+1) % self.number_of_players
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