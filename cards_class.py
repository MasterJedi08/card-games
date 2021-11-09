'''
just learned classes in my Software Dev class, so lets try this with classes!!
'''
import random as rand

class Card():
    __slots__ = ['rank', 'suit', 'name', 'shorthand']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
        if rank > 10:
            if rank == 11:
                self.name = 'Jack of ' + suit
                stub = 'J'
            elif rank == 12:
                self.name = 'Queen of ' + suit
                stub = 'Q'
            elif rank == 13:
                self.name = 'King of ' + suit
                stub = 'K'
            elif rank == 14:
                self.name = 'Ace of ' + suit
                stub = 'A'
            else:
                self.name = str(rank) + ' of ' + suit
        
        # if rank is alphabet -- take first letter
        if rank == 10:
            self.shorthand = str(rank) + suit[0]
        else:
            if rank > 10:
                self.shorthand = ' ' + stub + suit[0]
            else:
                rank = str(rank)
                self.shorthand = ' ' + rank[0] + suit[0]

        # display colors in python terminal based on suit
        if suit == 'Spades' or suit == 'Clubs':
            self.shorthand = '\033[34m' + self.shorthand + '\033[37m'
        else:
            self.shorthand = '\033[31m' + self.shorthand + '\033[37m'

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

def main():
    """
    main function
    """

if __name__ == '__main__':
    main()
# deck = Deck()
# for card in deck.cards:
#         print(card.shorthand, end=' ')
# deck.shuffle()
# print('shuffled:')
# for card in deck.cards:
#         print(card.shorthand, end=' ')