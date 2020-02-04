# Creating Pawn class -> Student or Master
# Pawns  - update_pos(*): updates the pawns own position
#        - remove_piece(): turns inPlay flag to false

class pawn:
    def __init__(self, color, pos, inPlay = True):
        self.color = color
        self.pos = pos
        self.inPlay = inPlay
        
    def update_pos(self,*new_pos):
        # new_pos => (row,column)
        self.pos = new_pos

    def remove_piece(self):
        self.inPlay = False

def create_pawns(color):
    #Blue pawns are on the row = 0
    #Red pawns are on the row = 4
    
    if color == 'Blue':
        row = 0
    elif color == 'Red':
        row = 4
    else:
        print("Must specify color!")
        return {}
    
    Pawns = {}
    
    #Pawns
    for i in range(4):
        entry = 'P' + str(i)    
        if i>1:
            position = [row,i+1]
        else:
            position = [row,i]
        Pawns[entry] = pawn(color,position)
    #Master
    entry = 'M'
    position = [row,2]
    Pawns[entry] = pawn(color,position)
    
    return Pawns



