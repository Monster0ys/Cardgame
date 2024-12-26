from __future__ import annotations
class Card():
    def __init__(self,num,color):
        self.number=num
        self.color=color
    def __str__(self):
        return str(self.number)+ ' ' + self.color 
    def __repr__(self):
        return self.__str__()
    def can_be_put_on_card(self,card:Card):
        if self.number == card.number or self.color == card.color:
            return True
        return False