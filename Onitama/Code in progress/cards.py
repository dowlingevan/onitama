# list of possible cards
# cards = ["boar","cobra","crab","crane",
#             "dragon","eel","elephant","frog",
#             "goose","horse","mantis","monkey",
#             "ox","rabbit","rooster","tiger"]

# Define movement patterns as a list of tuples
# referenced to a coordinate system where (0,0) is located in the upper left corner,
# x increase towards the left, y increases down
# card positioned from bottom players perspective
#
# To convert to the other players perspective, a  list comprehension can be used 
# to change the sign of all values
# This is the same as a 180 degree rotation
#


def get_cards():
    import random
    #Returns a list [(card_name,[moves]),...]
    # Cards are selected randomly
    
    cards = {
    'boar' : [(0,1),(-1,0),(0,1)],
    'cobra' : [(1,-1),(-1,0),(1,1)],
    'crab' : [(0,-1),(-2,0),(2,0)],
    'crane' : [(0,-1),(-1,1),(1,1)],
    'dragon' : [(-2,-1),(2,-1),(-1,1),(1,1)],
    'eel' : [(-1,-1),(1,0),(-1,1)],
    'elephant' : [(-1,-1),(1,-1),(-1,0),(1,0)],
    'frog' : [(-1,1),(-2,0),(1,1)],
    'goose' : [(-1,-1),(-1,0),(1,0),(1,1)],
    'horse' : [(0,-1),(-1,0),(0,1)],
    'mantis' : [(-1,-1),(1,-1),(0,1)],
    'monkey' : [(-1,-1),(1,-1),(-1,1),(1,1)],
    'ox' : [(0,-1),(1,0),(0,1)],
    'rabbit' : [(1,-1),(0,2),(-1,1)],
    'rooster': [(1,-1),(-1,0),(1,0),(-1,1)],
    'tiger': [(0,-2),(0,1)]
    }

    new_cards = random.sample(list(cards.items()),5)
    return (new_cards)


