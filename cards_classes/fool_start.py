# -*- coding: utf-8 -*-
from time import sleep
from fool_game import Cards,Player,Robot,Game

result = ''
winner = ''
player_name = ''
game_run = 'y'
#player_name = input("Введи своє ім'я:").capitalize()
deck = cards_player = cards_robot = []
trump_rob = trump_pla = trump = ''
######## Start ########
deck_game = Cards
# shuffle deck
deck = deck_game.shuffle_deck(deck_game)
# give cards for play's
deck_game.give_cards(deck_game)
cards_player, cards_robot = deck_game.cards_player,deck_game.cards_robot
cards_player.sort()
cards_robot.sort()
#make trump
trump = deck_game.make_trump(deck_game)
print("cards_player=%s" % cards_player)
print("cards_robot=%s" % cards_robot)
print("trump={}".format(trump))
print("deck_lenght=%s" % len(deck_game.deck))
print("deck_game=%s" % deck)
# define players
player = Player(deck,cards_player,trump)
robot = Robot(deck,cards_robot,trump)
# player see cards
player.see_cards(deck,cards_player,trump)

# determine younger trump
trump_pla = player.trump_player(cards_player,trump)
trump_rob = robot.trump_robot(cards_robot,trump)

print("trump_pla={} ; trump_rob={}".format(trump_pla,trump_rob))
