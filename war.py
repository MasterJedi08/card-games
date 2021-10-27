'''
text-based simulator of the game 'war' against computer
'''
import cards

def check_cards(player_card, dealer_card):
    """
    checks which of the two cards are higher, returns the winner
    """
    print('player card: ', player_card, 'dealer card:', dealer_card)
    player_card_rank = player_card[0][0]
    dealer_card_rank = dealer_card[0][0]
    print(player_card_rank, dealer_card_rank)

    if player_card_rank > dealer_card_rank:
        return 'player'
    elif player_card_rank < dealer_card_rank:
        return 'dealer'
    else:
        return 'war'

def go_to_war(player_hand, dealer_hand):
    """
    if cards are equal, place down three extra cards and flip over the fourth card
    highest fourth card wins all cards on table
    """
    print('------------ WAR!! ------------')
    # cards that are about to be drawn
    player_table_cards = []
    dealer_table_cards = []
    player_fourth = []
    dealer_fourth = []

    # draws 4 cards and puts them 'on the table' (into the table cards list)
    for _ in range(3):
        player_hand, player_table_cards = cards.top_draw(player_hand, player_table_cards)
        dealer_hand, dealer_table_cards = cards.top_draw(dealer_hand, dealer_table_cards)

    # get the fourth card (this card will be 'flipped over' to determine who wins war)
    player_hand, player_fourth = cards.top_draw(player_hand, player_fourth)
    dealer_hand, dealer_fourth = cards.top_draw(dealer_hand, dealer_fourth)

    print(' player/dealer fourth card:', player_fourth, dealer_fourth)

    # calls check_cards to see which card is higher and gets winner
    winner = check_cards(player_fourth, dealer_fourth)

    # adds the fourth card to the table cards so all can be added to the 
    player_table_cards.append(player_fourth)
    dealer_table_cards.append(dealer_fourth)

    # winner_check() where war_bool = True
    winner_check(winner, player_table_cards, dealer_table_cards, player_hand, dealer_hand, war_bool=False)

def take_winnings(winner, player_card, dealer_card, winner_hand, war_bool=False):
    """
    takes both cards and adds it to winner's hand
    """
    if war_bool == False:
        # adds both cards to bottom of winner hand
        winner_hand.append(player_card)
        winner_hand.append(dealer_card)

        # prints winner
        print('Player card:', player_card[0][3], '\nDealer card:', dealer_card[0][3])
        print('Winner:', winner)

    # war_bool is True
    else:
        # player_card/dealer_card is now not just one card, but a list of 4 cards, so iterate over all to add to winner hand
        for index in range(len(player_card)):
            winner_hand.append(player_card[index])
            winner_hand.append(dealer_card[index])
        
        # prints winner
        print('Player card:', player_card[0][3], '\nDealer card:', dealer_card[0][3])
        print('Winner:', winner)

    # returns to main

def winner_check(winner, player_card, dealer_card, player_hand, dealer_hand, war_bool=False):
    """
    based on what check_cards returns, add the cards to winner's hand OR go to war
    """
    if winner == 'player':
        take_winnings(winner, player_card, dealer_card, player_hand, war_bool)
    elif winner == 'dealer':
        take_winnings(winner, player_card, dealer_card, dealer_hand, war_bool)
    else:
        go_to_war(player_hand, dealer_hand)

def check_finish(player_hand, dealer_hand):
    """
    checks to see if there is a winner
    """
    # if player has no more cards in hand, dealer wins - game over
    if len(player_hand) == 0:
        print('Dealer wins game!')
        print('------------ GAME OVER ------------')
        return False
    # if dealer has no more cards in hand, player wins - game over
    elif len(dealer_hand) == 0:
        print('Player wins game!')
        print('------------ GAME OVER ------------')
        return False
    # otherwise, continue playing
    else:
        return True

def main():
    """
    runs simulator
    """
    # make deck and deal cards (21 card hand)
    deck = cards.make_deck()
    deck = cards.shuffle(deck)

    for card in deck:
        print(card[3], card)

    deck, player_hand, dealer_hand = cards.deal(deck, 21)

    print(len(player_hand), len(dealer_hand), len(deck))

    # variable to ensure that game ends when either player or dealer runs out of cards
    still_playing = True

    while still_playing == True:
        print('\n------------ Round begins ------------')

        # empty list that will contain value for card drawn
        player_card = []
        dealer_card = []

        # flip over top card of each hand
        player_hand, player_card = cards.top_draw(player_hand, player_card)
        dealer_hand, dealer_card = cards.top_draw(dealer_hand, dealer_card)

        # check which card is higher - if cards are equal: 'go to war'
        result = check_cards(player_card, dealer_card)
        winner_check(result, player_card, dealer_card, player_hand, dealer_hand)

        
        print('Cards in player hand:', str(len(player_hand)))
        print('Cards in dealer hand:', str(len(dealer_hand)))

        # continue until one player has all 52 cards
        still_playing = check_finish(player_hand, dealer_hand)

        # just to make it so everything doesn't appear at once
        input('\nEnd of round...click enter to continue')

if __name__ == '__main__':
    main()


'''
improvements: 

solve if double, triple, etc war
timing (so everything doesnt just appear at once)
'''