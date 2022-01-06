'''
Text-based blackjack simulator
'''
import cards

def hand_score(hand):
    """
    returns score of current hand based on blackjack rules
    """
    score = 0
    num_aces = 0

    for card in hand:
        rank = int(card[0])
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

    return score

def win_lose_or_draw(player_score, dealer_score):
    """
    determines who won the game
    """
    if player_score > 21:
        if dealer_score > 21:
            print('Draw')
        else:
            print('Dealer wins!')
    elif player_score == dealer_score:
        print('Draw')
    elif player_score > dealer_score:
        print('Player wins')
    else:
        print('Dealer wins')

def print_hand_and_score(player_name, hand):
    """
    prints player name, hand (in sorted order), and score of hand (and if player has busted)
    """
    score = hand_score(hand)

    print(player_name)
    for card in hand:
        print(card[3], end=' ')
    if score > 21:
        print('\nScore:', score, '(busted)')
    else:
        print('\nScore:', score)

def dealer_hit_or_stand(player_hand, dealer_hand):
    """
    determines if dealer will hit or stand
    """
    player_score = hand_score(player_hand)
    dealer_score = hand_score(dealer_hand)
    # if dealer score is under 17 OR dealer score < player score dealer will HIT
    if dealer_score < 17 or dealer_score < player_score:
        return True
    # otherwise, dealer stands
    else:
        return False

def player_hit_or_stand():
    """
    prompts user to hit or stand
    """
    while True:
        choice = input('Enter H for hit, S for stand: ')
        if choice == 'H' or choice == 'h':
            return True
        elif choice == 'S' or choice == 's':
            return False
    # choice = input('Enter H for hit, S for stand: ')
    # if choice == 'H' or choice == 'h':
    #     return True
    # elif choice == 'S' or choice == 's':
    #     return False
    # else:
    #     print('error check')
    #     player_hit_or_stand()


def main():
    """
    main function  -- runs one game of blackjack
    """
    # makes, shuffles, and cuts deck ... deals two hands of two cards from bottom half of the deck
    deck = cards.make_deck()
    deck = cards.shuffle(deck)
    top_half, bottom_half = cards.cut(deck)
    deck, player_hand, dealer_hand = cards.deal(bottom_half, 2)

    name = input('Enter your name: ')

    # prints hand and score for both player and dealer
    print_hand_and_score(name, player_hand)
    print_hand_and_score('Dealer', dealer_hand)

    # player and dealer decide to hit or stand (boolean value, Hit = True, Stand = False)
    player_choice = player_hit_or_stand()
    dealer_choice = dealer_hit_or_stand(player_hand, dealer_hand)

    # if player chose to hit, draw a card, print new hand, and calculate score; else, just calculate score
    if player_choice == True:
        print('Player hits')
        bottom_half, player_hand = cards.draw(bottom_half, player_hand)
        print_hand_and_score(name, player_hand)
        player_score = hand_score(player_hand)
    else:
        print('Player stands')
        player_score = hand_score(player_hand)

    # if dealer chose to hit, draw a card, print new hand, and calculate score; else, just calculate score
    if dealer_choice == True:
        print('Dealer hits')
        bottom_half, dealer_hand = cards.draw(bottom_half, dealer_hand)
        print_hand_and_score('Dealer', dealer_hand)
        dealer_score = hand_score(dealer_hand)
    else:
        print('Dealer stands')
        dealer_score = hand_score(dealer_hand)

    # determine who wins the game
    win_lose_or_draw(player_score, dealer_score)

    # comments below are testing stuff that i didn't wanna delete

    # print('\nhand 1:')
    # for card in hand1:
    #     print(card[3], end=' ')
    # print('\nhand 2:')
    # for card in hand2:
    #     print(card[3], end=' ')

    # print_hand_and_score('Legend', hand1)
    # print_hand_and_score('Rebel', hand2)

    # print(dealer_hit_or_stand(hand1, hand2))

    # win_lose_or_draw(hand_score(hand1), hand_score(hand2))

    # print(test())

if __name__ == '__main__':
    main()