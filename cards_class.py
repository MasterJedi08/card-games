import random as rand

class Card():
    __slots__ = ['__rank', '__suit', '__name']
    
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit
        
        if self.__rank > 10:
            if self.__rank == 11:
                self.__name = 'Jack of ' + self.__suit
            elif self.__rank == 12:
                self.__name = 'Queen of ' + self.__suit
            elif self.__rank == 13:
                self.__name = 'King of ' + self.__suit
            elif self.__rank == 14:
                self.__name = 'Ace of ' + self.__suit
            else:
                self.__name = str(self.__rank) + ' of ' + self.__suit
                
    # def __repr__(self):
    #     # longer version of printing the card is the full name
    #     return self.__name
      
    # how the card prints: shorthand -- 3 char rep of suit and rank
    def __str__(self):
        if self.__rank == 10:
            rep_string = str(self.__rank) + self.__suit[0] 
        else:
            rep_string = ' ' + str(self.__rank)[0] + self.__suit[0]
            
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

class Deck():
    __slots__ = ['__cards', '__length', '__top_half', '__bottom_half']

    def __init__(self):
        self.__cards = []
        self.__length = 52
        # top and bottom half are only used in specific games
        self.__top_half = []
        self.__bottom_half = []

        # creates list of 52 playing cards
        suit_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        
        for suit_val in suit_list:
            for rank_num in range(2, 15):
                card = Card(rank_num, suit_val)
                self.__cards.append(card)
                
    def get_length(self):
        return self.__length
        
    def __repr__(self):
        """
        prints all cards in deck
        """
        rep_string = ''
        for card in self.__cards:
            rep_string += card.__str__() + ' '
            
        return rep_string

    def shuffle(self):
        """
        return shuffled deck
        """
        rand.shuffle(self.__cards)

    def cut(self):
        """
        return cut halves of deck
        """
        if self.__length <= 1:
            pass
        else:
            mid = self.__length // 2
            self.__top_half = self.__cards[:mid]
            self.__bottom_half = self.__cards[mid:self.__length]
            
    # draw card functions
    def draw_card(self):
        """
        draw a card from deck
        """
        card = self.__cards.pop()
        self.__length -= 1
        
        return card
        
    def draw_top(self):
        """
        draw a card from top half of deck
        """
        card = self.__cards.pop()
        self.__length -= 1
        
        return card
                
    def draw_bottom(self):
        """
        draw a card from bottom half of deck
        """
        card = self.__cards.pop()
        self.__length -= 1
        
        return card

class Hand():
    __slots__ = ['__cards', '__score']

    def __init__(self):
        self.__cards = []
        self.__score = 0

    def __repr__(self):
        """
        prints all cards in hand
        """
        rep_string = ''
        for card in self.__cards:
            rep_string += card.__str__() + ' '
            
        return rep_string

    def __len__(self):
        return len(self.__cards)

    def deal_hand(self, deck, num):
        """
        deals a hand of num size from given deck
        """
        self.__cards = [deck.draw_card() for _ in range(num)]

    def draw_card(self, index):
        """
        draws card at specified index and removes it from hand
        """
        try:
            self.__cards.pop(index)
            return self.__cards[index]
        except:
            # if index out of range, just return none
            return None

# MISC TESTING STUFF - NOT NEEDED
#        
# deck = Deck()
# print(deck)
# deck.shuffle()
# print(deck)
# print(deck.draw_card())
# print(deck.draw_card())
# print(deck.draw_card())
# print(deck.draw_card())
# print(deck.draw_card())
# print(deck.draw_card())
# print(deck.draw_card())
# print(deck.draw_card())

# print(deck)
# print(deck.get_length())

# print(' ------------------------------------------- ')
# hand = Hand()
# hand.deal_hand(deck, 5)
# print(hand)
# print(hand.draw_card(0))
# print(hand)
# print(hand.draw_card(8))
# print(len(hand))