# -*- coding: utf-8 -*-
from time import sleep
from fool_game import *

result = ''
winner = ''
player_name = ''
game_run = 'y'
player_name = input("Введи своє ім'я:").capitalize()

i = 0
while not player_name.isalpha():
    player_name = input("Введи людське ім'я:").capitalize()
    if player_name.isalpha():
        print("Привіт, %s =)" % player_name)
        break
    if i == 2:
        print("OK!Дістав, привіт %s =)" % player_name)
        break
    i += 1

while game_run == 'y':
    print("Ок!Поїхали %s" % player_name)
    sleep(2)
    deck_cards, cards_player, cards_robot, trump = shuffle_give_cards()
    see_cards(deck_cards,cards_player,trump)
    trump_rob = trump_robot(cards_robot,trump)
    trump_pla = trump_player(cards_player,trump)
    step_player, step_robot = trumping(trump_pla,trump_rob,trump)

    while len(cards_robot) > 0 and len(cards_player) > 0:
        if step_robot:
            cards_robot = robot_attack(cards_robot,trump)
            result, cards_player = player_defence(cards_player,trump)
            if result == 'beat' or result == 'beat_trump':
                step_robot = False
                step_player = True
                sleep(2)
            elif result == 'take':
                sleep(2)
        else:
            cards_player = player_attack(cards_player,trump)
            result, cards_robot = robot_defence(cards_robot,trump)
            if result == 'beat' or result == 'beat_trump':
                step_robot = True
                step_player = False
                sleep(2)
            elif result == 'take':
                print("Холєра!Я забираю..")
                sleep(2)

        if len(deck_cards) > 0:
            if step_player:
                cards_robot,deck_cards = rob_take_card(cards_robot,deck_cards)
                cards_player,deck_cards = pla_take_card(cards_player,deck_cards)
            else:
                cards_player,deck_cards = pla_take_card(cards_player,deck_cards)
                cards_robot,deck_cards = rob_take_card(cards_robot,deck_cards)

        if len(cards_robot) > 0 and len(cards_player) > 0:
            see_cards(deck_cards,cards_player,trump)
        elif len(cards_robot) == 0 and len(cards_player) == 0:
            winner = 'NO'
            break
        elif len(cards_robot) > 0 and len(cards_player) == 0:
            winner = 'You'
            break
        elif len(cards_robot) == 0 and len(cards_player) > 0:
            winner = 'Me'
            break

    if winner == 'Me':
        game_run = input("Я виграв! Граємо далі? 'y'/'n':")
    elif winner == 'You':
        game_run = input("Вітаю %s!Ти виграв, граємо далі? 'y'/'n':" % player_name)
    elif winner == 'NO':
        game_run = input("Нічия!!! Граємо далі? 'y'/'n':")

    if game_run.lower() != 'y' and game_run.lower() != 'n':
        game_run = 'y'
    elif game_run.lower() == 'n':
        print("Па-па, дякую за гру!")
