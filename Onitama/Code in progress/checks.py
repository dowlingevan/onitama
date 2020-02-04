#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 14:53:21 2019

# Checks valid moves, captures, wins

@author: evandowling
"""

def check_bound(pos):
    # Check if piece is on board
    row = pos[0]
    column = pos[1] 
    return (-1<row<5 and -1<column<5)
 
def check_overlap(piece,pawns):
    # Check to see if one piece's location is on a teams pieces
    overlap_piece = None
    for label,pawn in pawns.items():
        if piece.pos == pawn.pos:
            overlap_piece = label
            break
    return overlap_piece

def check_win(Team1,Team2):
    # Check Team 1's winning conditions
    
    # Win by Stone
    if Team2['M'].inPlay == False:
        return True
    
    # Win by River 
    if Team1['M'].color == 'Blue':
        winpos = [4,2]
    else:
        winpos = [0,2]
        
    if Team1['M'].pos == winpos:
        return True
    
    return False
    
