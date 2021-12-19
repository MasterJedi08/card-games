from typing import Tuple
import goatils
import random as rand


COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    LEGENDARY : ORANGE + "L"}

class Card:
    __slots__ = ['__name', '__resource_cost', '__rarity', '__faction', '__attack', '__hp']
    
    def __init__(self, name, resource, rarity, faction, attack, hp):
        self.__name = name
        self.__resource_cost = resource
        self.__rarity = rarity
        self.__faction = faction
        self.__attack = attack
        self.__hp = hp
     
    # get methods 
       
    def get_name(self):
        return self.__name
    
    def get_resource_cost(self):
        return self.__resource_cost
    
    def get_rarity(self):
        return self.__rarity
    
    def get_faction(self):
        return self.__faction
    
    def get_attack(self):
        return self.__attack
    
    def get_hp(self):
        return self.__hp
    
    # one mutator method
    def set_hp(self, new_hp):
        self.__hp = new_hp
        
    # 2 diff card to string formats
    def __repr__(self):
        rep_string = (self.__name + '\nRarity: ' + self.__rarity + '\nFaction: ' + self.__faction +
        '\nResource Cost: ' + str(self.__resource_cost) + '\nAttack Power: ' + str(self.__attack) + '\nHP: ' + str(self.__hp))
        return rep_string
    
    def __str__(self):
        rep_string = ('[' + self.__faction[0] + self.__name[0] + ' ' + '{:02d}'.format(self.__resource_cost) +
        ' ' + '{:02d}'.format(self.__attack) + ' ' + '{:02d}'.format(self.__hp) + ']')
        return rep_string
    
    def damage(self, amount):
        """
        subtract damage from card hp
        """
        if amount <= self.__hp:
            self.__hp -= amount
            return 0
        else:
            current = self.__hp
            self.__hp = 0
            return amount - current
            
    def is_conscious(self):
        if self.__hp > 0:
            return True
        else:
            return False
        
    def __eq__(self, other):
        """
        cards are equal (return True) if all attributes (except name and hp) are same
        """
        if type(self) == type(other):
            if self.__attack == other.__attack and self.__faction == other.__faction and self.__rarity == other.__rarity and self.__resource_cost == other.__resource_cost:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        """
        sort by resource cost of cards, lowest to highest
        if costs are the same, compare by names
        """
        if type(self) == type(other):
            if self.__resource_cost == other.__resource_cost:
                return self.__name < other.__name
            else:
                return self.__resource_cost < other.__resource_cost
            
        return False
        
class Player:
    __slots__ = ['__name', '__score', '__resource_points', '__used_points', '__deck', '__hand', '__battalion', '__discarded']
    
    def __init__(self, name, deck):
        self.__name = name
        self.__score = 20
        self.__resource_points = 0
        self.__used_points = 0
        self.__deck = deck[:-5]
        self.__hand = deck[(len(deck)-4):]
        self.__battalion = []
        self.__discarded = []
        
    # printer functions
    def __repr__(self):
        rep_string = ('Player: ' + self.__name + '\nScore: ' + str(self.__score) + '\nResource Points: ' +
        str(self.__resource_points) + '/10' + '\nDeck: ' + str(len(self.__deck)) + '\nDiscarded: ' + 
        str(len(self.__discarded)) + '\nBattalion: ' + str([card.__str__() for card in self.__battalion]) + '\nHand: ' +
        str([card.__str__() for card in self.__hand]))
        
        return rep_string
        
    def __str__(self):
        return 'Player: ' + self.__name
    
    # get functions
    def get_name(self):
        return self.__name
    
    def get_battalion(self):
        return self.__battalion
     
    #  in game turn functions 
    def start_turn(self):
        """
        at start of turn: add 1 resource point, return any rsource points used, draw card and place in hand
        """
        # replenish resource points + 1
        self.__resource_points += self.__used_points
        self.__used_points = 0
        
        if self.__resource_points < 10:
            self.__resource_points += 1
        # draw card and add to hand
        self.draw_card()
         
    def draw_card(self):
        """
        draw a card and add it to hand
        """
        card = self.__deck[-1]
        self.__deck.pop()
        self.__hand.append(card)
        
    def play_card(self, card_index):
        """
        player provides card_index (1 - len(hand)), card is placed in battalion if cost is lower 
        than available resource points, and cost is subtracted from player resource points
        """
        card = self.__hand[card_index-1]
        cost = card.get_resource_cost()
        
        # add card to battalion if enough resource points to play card
        if cost <= self.__resource_points:
            # add card to battalion, take out of hand
            self.__battalion.append(card)
            self.__hand.pop(card_index-1)
            
            # subtract resource points used, add them to field used_points
            self.__resource_points -= cost 
            self.__used_points += cost  
                     
            print(card.__repr__())
            
        # otherwise, print 'not enough points' error 
        else:
            print('Not enough resource points to play card: ' + str(self.__resource_points) + '/10')

        
    def end_turn_attack_power(self):
        """
        determines player's damage at end of turn -- damage = total attack power of all cards in battalion
        """
        damage = 0
        
        for card in self.__battalion:
            damage += card.get_attack()
            
        return damage
    
    def take_damage(self, damage):
        """
        damage is taken from cards in battalion right to left -- if card's health reduced to 0, discard 
        if all cards in battalion have been defeated, subtract remaining damage from player score (can't go below 0)
        """
        while damage > 0:
            # reverse order range so it goes from left to right
            for index in range(len(self.__battalion)-1, -1, -1):
                card = self.__battalion[index]
                # get hp of card
                hp = card.get_hp()
                new_hp = hp - damage
                
                # if card hp reduced to 0, remove from battalion 
                if new_hp <= 0:
                    # remove card from battalion and add to discarded
                    self.__battalion.pop(index)
                    self.__discarded.append(card)
                else:
                    card.set_hp(new_hp)
                    
                # subtract card's hp from damage 
                damage -= hp   
                
            # if no cards left in battalion and damage > 0, subtract remaining damage from player score
            if len(self.__battalion) == 0 and damage > 0:
                self.__score -= damage
                # if subtracting damage made player score negative, set score to 0
                if self.__score < 0:
                    self.__score = 0  
                    
                damage = 0              
        
    def check_defeat(self):
        """
        if player score is 0 or they run out of cards, player loses
        """
        # player loses
        if self.__score == 0 or len(self.__deck) == 0:
            return True
        # player has not lost (yet)
        else:
            return False
        
    def return_card(self, location, index):
        """
        works for terminal commands H, B, and E 
        given location (hand, battalion), return card at given index
        """
        if location == 'hand':
            # NO OUT OF BOUNDS ERRORS
            if (index-1) < len(self.__hand):
                return self.__hand[index-1], True  
            else: 
                print('Card does not exist')
                return [], False  
        else:
            # NO OUT OF BOUNDS ERRORS
            if len(self.__battalion) > 0 and (index-1) < len(self.__hand):
                return self.__battalion[index-1], True
            else: 
                print('Card does not exist')
                return [], False
        
        
        
        
# make deck function -- not connected to a class
def make_deck(faction):
    """
    make deck of 40 cards: 20 common, 10 uncommon, 8 rare, 2 legendary
    num of health, attack, and resource based on rarity
    """
    deck = []
    # create 40 cards
    for card_number in range(41):
        # based on faction, determine name
        if faction == 'Goats':
            name = goatils.make_goat_name()
        else:
            troll_names = ['Troll', 'Troller', 'Trollzord', 'Trolling', 'Rick T-roll', 'Troll?', 'Trolled']
            name = troll_names[rand.randint(0, len(troll_names)-1)]
        
        # determine rarity - based on rarity find HP, attack (AP), resource cost (min HP=1, min attack=0)
        if card_number < 21:
            rarity = 'Common'
            # HP / AP - 8
            hp = rand.randint(1, 8)
            ap = 8 - hp
            # Resource Cost - btwn 1-3
            resource_cost = rand.randint(1, 3)
        elif card_number < 31:
            rarity = 'Uncommon'
            # HP / AP - 12
            hp = rand.randint(1, 12)
            ap = 12 - hp
            # Resource Cost - btwn 2-5
            resource_cost = rand.randint(2, 5)
        elif card_number < 39:
            rarity = 'Rare'
            # HP / AP - 16
            hp = rand.randint(1, 16)
            ap = 16 - hp
            # Resource Cost - btwn 4-7
            resource_cost = rand.randint(4, 7)
        else:
            rarity = 'Legendary'
            # HP / AP - 24
            hp = rand.randint(1, 24)
            ap = 24 - hp
            # Resource Cost - 10
            resource_cost = 10
        
        # create card
        card = Card(name, resource_cost, rarity, faction, ap, hp)  
        deck.append(card)
        
    # shuffle deck
    rand.shuffle(deck)
    return deck