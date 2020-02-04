####
#
# player objects have cards and pawns
#       - These cards and pawns can be updated
#
####

class player:
    def __init__(self,color,cards,pawns):
        self.color = color # Blue or red
        self.cards = cards # List of two or three cards, each an object
        self.pawns = pawns # Dict of all 5 pieces
        
    def update_cards(self,old_card,new_card):
        self.cards = self.cards.remove(old_card)
        self.cards = self.cards.append(new_card)
        
    def update_pawn(self,oldPawn_id,newPawn):
        #newPawn is the same pawn object with updated stats
        self.pawns[oldPawn_id] = newPawn
        
def create_players_pawns_cards():
    # Creates 5 random cards. First 2 are Blue Players, next 2 Red's, last is
    #   the extra.
    # Creates Pawns for each player
    # Assigns these cards and pawns to Player objects
    # Returns Blue player object, Red player object, extra card
    
    import cards
    import pawns
    
    cards = cards.get_cards()    
    BlueCards = cards[0:2]
    RedCards = cards[2:4]
    extra_card = cards[4]

    BluePawns = pawns.create_pawns('Blue')
    RedPawns = pawns.create_pawns('Red')
    
    BluePlayer = player('Blue',BlueCards,BluePawns)
    RedPlayer = player('Red',RedCards,RedPawns)
    
    return BluePlayer, RedPlayer, extra_card
    
    