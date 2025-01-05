from __future__ import annotations

colors = {
    "Red":"\033[38;5;1m",
    "Green":"\033[38;5;10m",
    "Blue":"\033[38;5;21m",
    "Yellow":"\033[38;5;227m",
    "END":"\033[39m"
}

class Card():
    def __init__(self,name:str,color:str,function:callable):
        self.name:str=name
        self.color:str=color
        self.function:callable=function
    def __str__(self):
        return str(self.name) + ' ' + colors[self.color] + self.color + colors["END"]
    def __repr__(self):
        return self.__str__()
    def can_be_put_on_card(self,card:Card):
        if self.name == card.name or self.color == card.color:
            return True
        return False