import gvt

def main():
    goat = gvt.Card('goat', 45, 'legendary', 'goat', 15, 10)
    not_goat = gvt.Card('not goat', 15, 'normal', 'troll', 25, 30)
    similar_goat = gvt.Card('similar goat', 45, 'legendary', 'goat', 15, 10)
    what_goat = gvt.Card('what goat', 30, 'fancy', 'goat', 75, 5)
    
    print(goat)
    
    goat.damage(not_goat.get_attack())
    print(goat.get_hp())
    not_goat.damage(goat.get_attack())
    print(not_goat.get_hp())
    print(goat == similar_goat)
    print(goat == not_goat)
    
    hand = [goat, not_goat, similar_goat, what_goat]
    hand.sort()
    
    for card in hand:
        print(card)
    
main()