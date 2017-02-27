# -*- coding: utf-8 -*-
from os import system
from time import sleep
from fool_game import Cards

result = ''
winner = ''
player_name = ''
game_run = 'y'
#player_name = input("Введи своє ім'я:").capitalize()
cards_player = []
cards_robot = []

deck_rand = Cards
# shuffle deck
deck_rand.shuffle_deck()
#print("deck_game=%s" % deck_game)
for i in range(6):
    cards_player = deck_rand.give_cards_pla()
    print("cards_player=%s" % cards_player)
    cards_robot = deck_rand.give_cards_rob()
    print("cards_robot=%s" % cards_robot)

#print("deck_game=%s" % deck_game)
#print("cards_player=%s" % cards_player)
#print("cards_robot=%s" % cards_robot)
