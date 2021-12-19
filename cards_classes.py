import random as rand

class Card():
    __slots__ = ['__rank', '__suit', '__name']
    
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        
        if self.__rank > 10:
            if self.__rank == 11:
                self.name = 'Jack of ' + self.__suit
            elif self.__rank == 12:
                self.name = 'Queen of ' + self.__suit
            elif self.__rank == 13:
                self.name = 'King of ' + self.__suit
            elif self.__rank == 14:
                self.name = 'Ace of ' + self.__suit
            else:
                self.name = str(self.__rank) + ' of ' + self.__suit
                
        
    # how the card prints: shorthand -- 3 char rep of suit and rank
    def __str__(self):
        if self.__rank == 10:
            rep_string = str(self.__rank[0]) + self.__suit[0] 
        else:
            rep_string = ' ' + str(self.__rank[0]) + self.__suit[0]
            
        # display colors in python terminal based on __suit
        if self.__suit == 'Spades' or self.__suit == 'Clubs':
            rep_string = '\033[34m' + rep_string + '\033[37m'
        else:
            rep_string = '\033[31m' + rep_string + '\033[37m'

        return rep_string
        
    # comparing cards    
    def __eq__(self, other):
        # two cards are equal if same suit and rank (so they'd have the same name)
        if type(self) == type(other):
            if self.__name == other.__name:
                return self.__name == other.__name
        return False
    
    def __lt__(self, other):
        # a card is less than the other based on rank
        if type(self) == type(other):
            if self.__rank < other.__rank:
                return self.__rank < other.__rank
        return False
    
    def __gt__(self, other):
        # a card is greater than the other based on rank
        if type(self) == type(other):
            if self.__rank > other.__rank:
                return self.__rank > other.__rank
        return False
    