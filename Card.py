from __future__ import annotations
class Card():
    def __init__(self,name:str,color:str,function:callable):
        self.name:str=name
        self.color:str=color
        self.function:callable=function
    def __str__(self):
        return str(self.name)+ ' ' + self.color 
    def __repr__(self):
        return self.__str__()
    def can_be_put_on_card(self,card:Card):
        if self.name == card.name or self.color == card.color:
            return True
        return False