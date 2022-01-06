'''
Author: MasterJedi08 on GitHub

Description: a text-based blackjack simulator 
Note: a lot of this code is taken from the previous version of this 
module, found in thedoesnt_use_classes folder as X_blackjack.py
'''
import cards_class as cards
from doesnt_use_classes.cards import deal

def calculate_score(hand):
    """
    calculates score of cards in given hand (based on blackjack rules)
    returns True if busted 
    """
    score = 0
    num_aces = 0

    for card in hand.get_cards():
        rank = card.get_rank()
        # score for number rank = rank
        if rank <= 10:
            score += rank
        elif rank == 14:
            # score for ace = 11 DEPENDENT ON SCORE 
            num_aces += 1    
        # score for face cards = 10
        else:
            score += 10

    # if there are aces: 
    if num_aces > 0:
        added_11 = False
        for ace in range(num_aces):
            # if adding 11 to score would make player bust, add 1
            if score + 11 > 21:
                score += 1
            # if adding 11 to score would NOT make player bust and
            # an ace has not been counted as 11 points yet, add 11
            elif score + 11 < 21 and added_11 == False:
                score += 11
                added_11 = True

    hand.modify_score(score)

    # returns True if busted
    if score > 21: 
        print(score)
        return True

    return False

def bust(player_bool, player_hand, dealer_bool, dealer_hand):
    """
    calls winner if busted
    """
    if dealer_bool == True and player_bool == True:
        draw(player_hand, dealer_hand, True)
    elif dealer_bool:
        winner('Player', player_hand, 'Dealer', dealer_hand, True)
    elif player_bool:
        winner('Dealer', dealer_hand, 'Player', player_hand, True)
    else:
        return None

def dealer_hit_or_stand(player_hand, dealer_hand, deck):
    """
    determines if dealer will hit or stand
    """
    # if dealer score is under 17 OR dealer score < player score dealer will HIT
    if dealer_hand.get_score() < 17 or dealer_hand.get_score() < player_hand.get_score():
        return hit(dealer_hand, deck)
    # otherwise, dealer stands
    else:
        return dealer_hand.get_score() > 21

def player_hit_or_stand(player_hand, deck):
    """
    prompts user to hit or stand (will repeat until correct input is given)
    """
    valid_input = False
    while not valid_input:
        choice = input('Enter H for hit, S for stand: ')
        if choice == 'H' or choice == 'h':
            return hit(player_hand, deck)
        elif choice == 'S' or choice == 's':
            return player_hand.get_score() > 21  

def hit(hand, deck):
    """
    draw new card, recalculate score, returns True if bust
    """
    hand.add_card(deck)
    print(hand)
    return calculate_score(hand)     


def winner(winner, winner_hand, loser, loser_hand, busted=False):
    """
    prints winner
    """
    print("------------ RESULTS ------------")
    print(winner, 'wins:', winner_hand, '\tScore:', winner_hand.get_score())
    if busted:
        print('[BUSTED]', end= ' ')
    print(loser, 'lost:', loser_hand, '\tScore:', loser_hand.get_score())
    print("------------ END OF GAME ------------")
    exit()

def draw(player_hand, dealer_hand, bust=False):
    print('------------ RESULTS ------------')
    print('<DRAW>')
    if bust:
        print("[BUSTED] Dealer:", dealer_hand, '\tScore:', dealer_hand.get_score(), "\n[BUSTED] Player:", player_hand, '\tScore:', player_hand.get_score())
    else:
        print("Dealer:", dealer_hand, '\tScore:', dealer_hand.get_score(), "\nPlayer:", player_hand, '\tScore:', player_hand.get_score())
    print("------------ END OF GAME ------------")
    exit()

def determine_winner(player_hand, dealer_hand):
    """
    if neither has busted yet, and player and dealer have chosen to hit or stand,
    decide who has higher 
    """
    player_score = player_hand.get_score()
    dealer_score = dealer_hand.get_score()
    if player_score > dealer_score:
        winner('Player', player_hand, 'Dealer', dealer_hand)
    elif dealer_score > player_score:
        winner('Dealer', dealer_hand, 'Player', player_hand)
    else:
        draw(player_hand, dealer_hand, False)

def main():
    """
    main function  -- runs one game of blackjack
    """
    # makes, shuffles, and cuts deck
    deck = cards.Deck()
    deck.shuffle()
    deck.cut()

    # deals two hands of two cards from bottom half of the deck
    player_hand = cards.Hand()
    dealer_hand = cards.Hand()
    player_hand.deal_hand_bottom(deck, 2)
    dealer_hand.deal_hand_bottom(deck, 2)

    # print player hand and score
    print('Player Hand: ', player_hand)
    print('Dealer Hand: ', dealer_hand)

    # check if either dealer or player has busted
    player_bust = calculate_score(player_hand)
    dealer_bust = calculate_score(dealer_hand)
    bust(player_bust, player_hand, dealer_bust, dealer_hand)

    # hit or stand
    player_bust = player_hit_or_stand(player_hand, deck)
    dealer_bust = dealer_hit_or_stand(player_hand, dealer_hand, deck)
    print(player_bust, ':', player_hand.get_score())
    print(dealer_bust, ':', dealer_hand.get_score())
    bust(player_bust, player_hand, dealer_bust, dealer_hand)

    # determine who wins game
    determine_winner(player_hand, dealer_hand)

    # end of game

if __name__ == '__main__':
    main()