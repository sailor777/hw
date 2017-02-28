# -*- coding: utf-8 -*-
from random import choice,randint,shuffle
#from os import system

class Cards:
    deck = ['C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
            'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
            'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
            'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
            ]
    deck_weighted = ['C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
                     'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
                     'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
                     'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
                     ]
    card_ranks = [ '6','7','8','9','T','J','Q','K','A' ]
    cards_rob_ranks = {'6':0,'7':0,'8':0,'9':0,'T':0,'J':0,'Q':0,'K':0,'A':0}
    draw_map_suit = {'C': '\u2667','D': '\u2666','H': '\u2665','S': '\u2664'}
    cards_robot = []
    cards_player = []
    trump = ''

    def __init__(self):
        self.deck = deck

    def shuffle_deck(self):
        for i in range(10):
            shuffle(self.deck)
        return self.deck

    def give_cards_rob(self):
        self.cards_robot.append(self.deck[-1])
        self.deck.pop()
        return self.cards_robot

    def give_cards_pla(self):
        self.cards_player.append(self.deck[-1])
        self.deck.pop()
        return self.cards_player

    def make_trump(self):
        self.trump = self.deck[randint(0,len(self.deck)-1)]
        self.deck.remove(self.trump)
        self.deck.insert(0,self.trump)
        return self.trump

class Player:
    pass

class Robot:
    pass

class Game:
    cardgame = []
    pass
