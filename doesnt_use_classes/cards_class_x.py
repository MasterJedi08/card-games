'''
just learned classes in my Software Dev class, so lets try this with classes!!
'''
import random as rand

class Card():
    __slots__ = ['__rank', 'suit', 'name', '__shorthand']

    def __init__(self, __rank, suit):
        self.__rank = __rank
        self.suit = suit
        
        if __rank > 10:
            if __rank == 11:
                self.name = 'Jack of ' + suit
                stub = 'J'
            elif __rank == 12:
                self.name = 'Queen of ' + suit
                stub = 'Q'
            elif __rank == 13:
                self.name = 'King of ' + suit
                stub = 'K'
            elif __rank == 14:
                self.name = 'Ace of ' + suit
                stub = 'A'
            else:
                self.name = str(__rank) + ' of ' + suit
        
        # if __rank is alphabet -- take first letter
        if __rank == 10:
            self.__shorthand = str(__rank) + suit[0]
        else:
            if __rank > 10:
                self.__shorthand = ' ' + stub + suit[0]
            else:
                __rank = str(__rank)
                self.__shorthand = ' ' + __rank[0] + suit[0]

        # display colors in python terminal based on suit
        if suit == 'Spades' or suit == 'Clubs':
            self.__shorthand = '\033[34m' + self.__shorthand + '\033[37m'
        else:
            self.__shorthand = '\033[31m' + self.__shorthand + '\033[37m'

    def __str__(self):
        return self.__shorthand


class Deck():
    __slots__ = ['cards', 'top_half', 'bottom_half']

    def __init__(self):
        self.cards = []

        # creates list of 52 playing cards
        suit_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        for suit_val in suit_list:
            for rank_num in range(2, 15):
                card = Card(rank_num, suit_val)
                self.cards.append(card)

    def shuffle(self):
        """
        return shuffled deck
        """
        rand.shuffle(self.cards)

    def cut(self):
        """
        return cut halves of deck
        """
        length = len(self.cards)

        if length <= 1:
            pass
        else:
            mid = length // 2
            self.top_half = self.cards[:mid]
            self.bottom_half = self.cards[mid:length]

    def print_deck(self):
        """
        prints all cards in deck
        """
        for card in self.cards:
            print(card.__shorthand, end=' ')


class Hand():
    __slots__ = ['cards', 'score']

    def __init__(self):
        self.cards = []
        self.score = 0

    def draw(self, deck):
        """
        draw one card from deck and add to hand 
        """
        if len(deck.cards) == 0:
            return None
        else:
            card = deck.cards.pop(len(deck.cards)-1)
            self.cards.append(card)

    def deal_hand(self, deck, num):
        """
        deal hand of num cards 
        """
        count_hand = 0
        while count_hand < num:
            self.draw(self, deck)
            count_hand += 1

    def print_hand(self):
        """
        prints all cards in hand
        """
        for card in self.cards:
            print(card.__shorthand, end=' ')

def main():
    """
    main function
    """

if __name__ == '__main__':
    main()
# deck = Deck()
# for card in deck.cards:
#         print(card.__shorthand, end=' ')
# deck.shuffle()
# print('shuffled:')
# for card in deck.cards:
#         print(card.__shorthand, end=' ')