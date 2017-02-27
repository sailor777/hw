# -*- coding: utf-8 -*-
from os import system
from time import sleep
from fool_game import Cards

result = ''
winner = ''
player_name = ''
game_run = 'y'
#player_name = input("Введи своє ім'я:").capitalize()
deck = []
cards_player = []
cards_robot = []

deck_game = Cards
# shuffle deck
deck = deck_game.shuffle_deck(deck_game)
for i in range(6):
    deck_game.give_cards_pla(deck_game)
    deck_game.give_cards_rob(deck_game)

cards_player = deck_game.cards_player
cards_robot = deck_game.cards_robot

print("cards_player=%s" % cards_player)
print("cards_robot=%s" % cards_robot)

print("deck_lenght=%s" % len(deck_game.deck))
print("deck_game=%s" % deck_game.deck)
