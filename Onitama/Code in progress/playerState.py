class player:
    def __init__(self,color,cards):
        self.color = color # Blue or red
        self.cards = cards # a list of two or three cards, each an object
    
    def update_cards(self,old_card,new_card):
        self.cards = self.cards.remove(old_card)
        self.cards = self.cards.append(new_card)
        
def create_players_w_Cards():
    
    import cards
    cards = cards.get_cards()
    
    BluePlayer = player('Blue',cards[0:2])
    RedPlayer = player('Red',cards[2:4])
    extra_card = cards[4]
    
    return BluePlayer, RedPlayer, extra_card
    
    