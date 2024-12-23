class Card():
    def __init__(self,num,color):
        self.number=num
        self.color=color
    def __str__(self):
        return str(self.number)+ ' ' + self.color 
    def __repr__(self):
        return self.__str__()