def updatePosition(pawn,position):
    pawn.pos = positioned
    # do I need a return statement here?

def checkCapture(position,turn):
    color = x['defence']
    for p in Pawns[color]:
        if position == p.pos:
            # remove piece from play
            Pawns[color].remove(p)
        # do I need anything else here?

def endTurn():
