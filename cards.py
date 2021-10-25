'''
module that deals with cards: creates cards and deck, shuffles deck, deals 2 hands
'''

import random as rand

def make_card(rank, suit):
    """
    create new card given rank and suit, return card with rank, suit, name, and shorthand
    """
    #TODO: create name (rank + of + suit)
    if rank > 10:
        if rank == 11:
            name = 'Jack of ' + suit
            stub = 'J'
        elif rank == 12:
            name = 'Queen of ' + suit
            stub = 'Q'
        elif rank == 13:
            name = 'King of ' + suit
            stub = 'K'
        elif rank == 14:
            name = 'Ace of ' + suit
            stub = 'A'
    else:
        name = str(rank) + ' of ' + suit

    #TODO: create shorthand (rank + first letter of suit)
    # if rank is alphabet -- take first letter
    if rank == 10:
        shorthand = str(rank) + suit[0]
    else:
        if rank > 10:
            shorthand = ' ' + stub + suit[0]
        else:
            rank = str(rank)
            shorthand = ' ' + rank[0] + suit[0]

    if shorthand[2] == 'S' or shorthand[2] == 'C':
        shorthand = '\033[34m' + shorthand + '\033[37m'
    else:
        shorthand = '\033[31m' + shorthand + '\033[37m'

    card = (rank, suit, name, shorthand)

    return card

def make_deck():
    """
    creates and returns standard 52 card deck
    """
    suit_list = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    deck = []

    for suit_val in suit_list:
        for rank_num in range(2, 15):
            card = make_card(rank_num, suit_val)
            deck.append(card)

    return deck

def shuffle(deck):
    """
    shuffles the deck
    """
    for i in range(len(deck)-1):
        rand_index = rand.randint(0, 51)
        holder = deck[i]
        deck[i] = deck[rand_index]
        deck[rand_index] = holder

    return deck

def draw(deck, hand):
    """
    draw card from 'bottom' of the deck and adds it to the hand, returns deck and hand
    """
    if len(deck) == 0:
        return None
    else:
        card = deck.pop(len(deck)-1)
        hand.append(card)
        
    return deck, hand

def deal(deck, num):
    """
    creates two hands and alternates dealing to both hands, return both hands and deck
    """
    hand1 = []
    hand2 = []

    count_hand1 = 0
    count_hand2 = 0
    while count_hand1 <= num and count_hand2 <= num:
        deck, hand1 = draw(deck, hand1)
        count_hand1 += 1
        deck, hand2 = draw(deck, hand2)
        count_hand2 += 2
        # if count % 2 == 0:
        #     deck, hand1 = draw(deck, hand1)
        #     count += 1
        # else:
        #     deck, hand2 = draw(deck, hand2)
        #     count += 1

    return deck, hand1, hand2

def cut(deck):
    """
    cuts deck into two halves
    """
    length = len(deck)

    if length <= 1:
        raise(ValueError)
    else:
        mid = length // 2
        top_half = deck[:mid]
        bottom_half = deck[mid:length]

    return top_half, bottom_half

def main():
    deck = make_deck()
    deck = shuffle(deck)

    print('\nbefore dealing:')
    for card in deck:
        print(card[3], end=' ')

    deck, hand1, hand2 = deal(deck, 8)

    print('\nhand 1:')
    for card in hand1:
        print(card[3], end=' ')
    print('\nhand 2:')
    for card in hand2:
        print(card[3], end=' ')
    print('\ndeck:', len(deck))
    for card in deck:
        print(card[3], end=' ')

    half1, half2 = cut(deck)
    print('\nhalf1:')
    for card in half1:
        print(card[3], end=' ')
    print('\nhalf2:')
    for card in half2:
        print(card[3], end=' ')

if __name__ == '__main__':
    main()