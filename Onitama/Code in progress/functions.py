def updatePosition(pawn,position):
    import checks
    
    

def checkCapture(position,turn):
    color = x['defence']
    for p in Pawns[color]:
        if position == p.pos:
            # remove piece from play
            Pawns[color].remove(p)
        # do I need anything else here?

def endTurn():
