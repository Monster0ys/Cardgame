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
    def __init__(self,number_of_players:int):
        self.number_of_players=number_of_players
        self.create_deck()
        self.shuffle_deck()
        for i in range(number_of_players):
            self.players.append(Player())
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
    def check_card_compatibility(self, players_card:Card):
        if self.get_card_from_table().number == players_card.number or self.get_card_from_table().color == players_card.color:
            return True
        return False
    def players_turn(self, player:Player,number_of_card:int):
        if self.check_card_compatibility(player.hand[number_of_card]) and player==self.get_current_player():
            self.cards_on_table.append(player.hand.pop(number_of_card))
            self.set_next_player()
    def get_current_player(self):
        return self.players[self.current_player]
    def set_next_player(self):
        self.current_player=(self.current_player+1) % self.number_of_players
    def get_card_from_table(self):
        return self.cards_on_table[-1]
    def player_turn_interface(self):
        print("\033[2J\033[H", end="")
        print(f'Player: {self.current_player}')
        print(self.get_current_player())
        print(f'Card on table: {self.get_card_from_table()}')
        pick=int(input("Enter card number: "))
        if pick >= 0 and pick < len(self.get_current_player().hand):
            self.players_turn(self.get_current_player(),pick)
        elif pick == -1:
            self.add_card_to_player(self.get_current_player())
        else:
            self.set_next_player()
    def run(self):
        game_finish=False
        while not game_finish:
            self.player_turn_interface()
            for player in self.players:
                if len(player.hand)==0:
                    game_finish=True