import gvt

# terminal commands used by 
TERMINAL_COMMANDS = ("terminal commands:" + 
"\nH # - show detailed string of given card in player hand (# is 1 - length of hand)" + 
"\nB # - show detailed string of given card in player battalion (# is 1 - length of battalion)" + 
"\nE # - show detailed string of given card in enemy battalion (# is 1 - length of enemy battalion)" +
"\nP #  - play card from hand - if card played succesfully, print detailed string of played card, otherwise print error" +
"\nQ - end turn" + "I - display list of commands")

def take_turn(player, enemy):
    """
    displays player __repr__, prompts player to enter commands, handles player input
    """
    # start of turn reqs (draw card, replenish resource points)
    player.start_turn()
    # display __repr__ of player
    print('\n------------Player turn: ' + player.get_name() +'------------\nPLAYER STATS:')
    print(player.__repr__())
    
    # continuously asks for commands until turn ends
    while True:
        # enter commands - list of commands at bottom of script
        player_command = input('\n' + player.get_name() + ' - enter command >> ')
        player_command = player_command.split(' ')
        command_function = player_command[0]
        
        # if not Q or I, a number should follow
        if len(player_command) > 1:
            # making sure there's no out of bounds errors
            if player_command[1] == 0:
                player_command[1] == 1
                
            # print card in hand
            if command_function == 'H' or command_function == 'h':
                card, bool = player.return_card('hand', int(player_command[1]))
                if bool:
                    print(card.__repr__())
            
            # print card in battalion 
            elif command_function == 'B' or command_function == 'b':
                card, bool = player.return_card('battalion', int(player_command[1]))
                # if not an empty battalion, print card
                if bool:
                    print(card.__repr__())
            
            # print card in enemy battalion
            elif command_function == 'E' or command_function == 'e':
                card, bool = enemy.return_card('hand', int(player_command[1]))
                if bool:
                    print(card.__repr__())
            
            # play card
            elif command_function == 'P' or command_function == 'p':
                player.play_card(int(player_command[1]))
            
            # if none of the above, error
            else:
                print('<< Invalid command >>')
        else:
            # end turn 
            if command_function == 'Q' or command_function == 'q':
                # if cards in player battalion, attack enemy player
                if len(player.get_battalion()) != 0:
                    print('\n' + player.__str__() + ' ATTACKS ' + enemy.__str__())
                    
                    attack = player.end_turn_attack_power()
                    enemy.take_damage(attack)
                # only command that will return to main and officially end turn
                return
            # display terminal commands
            elif command_function == 'I' or command_function == 'i':
                print(TERMINAL_COMMANDS)
            else:
                print('<< Invalid command >>')
                    
                

def main():
    """
    plays Goats vs Trolls
    """
    # prompt players to enter name
    p1_name = input('Player 1 - Enter name: ')
    p2_name = input('Player 2 - Enter name: ')
    
    # P1 = goats, P2 = trolls - create players
    deck_1 = gvt.make_deck('Goats')
    player_1 = gvt.Player(p1_name, deck_1)
    
    deck_2 = gvt.make_deck('Trolls')
    player_2 = gvt.Player(p2_name, deck_2)
    
    # while neither player has been defeated, take turns
    while player_1.check_defeat() == False and player_2.check_defeat() == False:
        take_turn(player_1, player_2)
        
        print()
        
        take_turn(player_2, player_1)
        
    print('------------GAME OVER------------')
    if player_1.check_defeat():
        print(player_2.get_name() + ' WINS')
    else:
        print(player_1.get_name() + ' WINS')
    
if __name__ == '__main__':
    main()
    
'''
terminal commands:

H # - show __repr__ of given card (index '#') in player hand (# is 1 - len(hand))

B # - show __repr__ of given card (index '#') in player battalion (# is 1 - len(hand))

E # - show __repr__ of given card (index '#') in enemy battalion (# is 1 - len(hand))

P #  - play card from hand - if card played succesfully, print __repr__ of played card, otherwise print error

Q - end turn

I - display list of commands
'''

